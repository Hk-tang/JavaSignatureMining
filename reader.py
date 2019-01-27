from pydriller import RepositoryMining, GitRepository
import csv
import sys
import re

# pydriller should be able to access the remote repos
# but I had a problem with permissions on my system and
# had to clone them manually
# repos = ["https://github.com/spring-projects/spring-boot.git",
#         "https://github.com/spring-projects/spring-framework.git"]

# Taken from: https://stackoverflow.com/questions/68633/regex-that-will-match-a-java-method-declaration
# On 01/26/2019
signature_pattern = "(public|protected|private|static|\s) +[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *(\{?|[^;])"
parameters_pattern = "\((.*?)\)"
signature_changes = []

# Get all repos from command line arguments
repos = sys.argv[1:]
for repo in repos:
    project_name = ""
    for commit in RepositoryMining(repo, only_no_merge=True,
                                   only_modifications_with_file_types=[
                                       '.java']).traverse_commits():
        project_name = commit.project_name
        signature_changes = []
        gr = GitRepository(repo)
        for modified_file in commit.modifications:
            # if modified_file.methods:
            #     print(modified_file.methods[0].parameters)
            diff = gr.parse_diff(modified_file.diff)
            # There can not be a change in signature
            # if there are no additions or no deletions
            if diff['added'] and diff["deleted"]:
                line_changes = []
                for line_added in diff['added']:
                    for line_deleted in diff['deleted']:
                        if line_added[0] == line_deleted[0]:
                            line_changes.append((line_added, line_deleted))
                for line in line_changes:
                    addition = line[0][1].strip()
                    deletion = line[1][1].strip()
                    # If found then add to signature changes
                    if re.search(signature_pattern, addition) and \
                            re.search(signature_pattern, deletion):
                        params_new = re.search(parameters_pattern, addition)
                        params_old = re.search(parameters_pattern, deletion)
                        if params_new and params_old:
                            params_new = params_new.group(0).replace("(", "")\
                                .replace(")", "").split(",")
                            params_old = params_old.group(0).replace("(", "")\
                                .replace(")", "").split(",")
                            if len(params_new) != len(params_old):
                                signature_changes.append((commit.hash,
                                                          modified_file.filename,
                                                          deletion,
                                                          addition))

    with open("results/" + project_name + "_results.csv", "w") as results_file:
        csv_writer = csv.writer(results_file)
        # Add Header row to csv
        csv_writer.writerow(['Commit SHA',
                             'Java File',
                             'Old function signature',
                             'New function signature'])
        for change in signature_changes:
            csv_writer.writerow([change[0],
                                 change[1],
                                 change[2],
                                 change[3]])
