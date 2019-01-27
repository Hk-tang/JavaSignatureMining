from pydriller import RepositoryMining, GitRepository
from pprint import pprint
import csv

# pydriller should be able to access the remote repos
# but I had a problem with permissions on my system and
# had to clone them manually
# repos = ["https://github.com/spring-projects/spring-boot.git",
#         "https://github.com/spring-projects/spring-framework.git"]
repos = ["..\\Repos\\fescar"]

for repo in repos:
    for commit in RepositoryMining(repo, only_no_merge=True,
                                   only_modifications_with_file_types=[
                                        '.java'
                                   ]).traverse_commits():
        with open("results/" + commit.project_name + "_results.csv", "w") \
                as results_file:
            csv_writer = csv.writer(results_file)
            # Add Header row to csv
            csv_writer.writerow(['Commit SHA',
                                 'Java File',
                                 'Old function signature',
                                 'New function signature'])
            gr = GitRepository(repo)
            for modified_file in commit.modifications:
                # diff = gr.parse_diff(modified_file.diff)
                print(commit.hash, modified_file.diff)
                # pprint(diff)
