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

# Get all repos from command line arguments
repos = sys.argv[1:]
for repo in repos:
    project_name = ""
    signature_changes = []
    for commit in RepositoryMining(repo, only_no_merge=True,
                                   only_modifications_with_file_types=[
                                       '.java']).traverse_commits():
        project_name = commit.project_name
        gr = GitRepository(repo)
        for modified_file in commit.modifications:
            # if modified_file.methods:
            #     print(modified_file.methods[0].parameters)
            diff = gr.parse_diff(modified_file.diff)
            # There can not be a change in signature if there are
            # no additions or no deletions
            if diff['added'] and diff["deleted"]:
                for line_added in diff['added']:
                    for line_deleted in diff['deleted']:
                        # Check if the line change is a method signature
                        old_signature = re.search(signature_pattern, line_deleted[1])
                        new_signature = re.search(signature_pattern, line_added[1])
                        if new_signature and old_signature:
                            method_name_added = re.search("^[^(]+", new_signature.group(0).strip())
                            method_name_deleted = re.search("^[^(]+", old_signature.group(0).strip())
                            # Check if the method names are the same
                            if method_name_added and method_name_deleted and method_name_added.group(0) == method_name_deleted.group(0):
                                # Get the parameters of the method signatures
                                params_new = re.search(parameters_pattern, line_added[1])
                                params_old = re.search(parameters_pattern, line_deleted[1])
                                # If statement is not necessary but there is a danger if
                                # we weren't able to find the method parameters
                                if params_new and params_old:
                                    params_new = params_new.group(0).split(",")
                                    params_old = params_old.group(0).split(",")
                                    # If parameters were added then add to list
                                    if len(params_new) > len(params_old):
                                        signature_changes.append((commit.hash,
                                                                  modified_file.filename,
                                                                  line_deleted[1],
                                                                  line_added[1]))

    # With statement automatically closes file when finished
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
