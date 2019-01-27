Description:
This is a small project intended to report the changes in method signatures of
a Java repository. It uses the pydriller library for easy APIs into accessing
Git information such as commit hashes and diffs.

Installation and Usage:
This project requires no building or installation

To run the program run this line in a terminal opened to the path of this
project: "python3 reader.py <repo1 repo2 ...>"
Arguments to the program are either the Git repo's http url or a path on
your system to a Git repository.
You can enter multiple repositories separated by a space.

This repository has already inspected two repositories (under the results directory):
    1. Spring Framework repository
        ("https://github.com/spring-projects/spring-framework")
    2. Spring-Boot repository
        ("https://github.com/spring-projects/spring-boot")

Contributor list:
    Henry Tang (hktang@ualberta.ca)

@inbook{PyDriller,
	title = "PyDriller: Python Framework for Mining Software Repositories",
	abstract = "Software repositories contain historical and valuable information about the overall development of software systems. Mining software repositories (MSR) is nowadays considered one of the most interesting growing fields within software engineering. MSR focuses on extracting and analyzing data available in software repositories to uncover interesting, useful, and actionable information about the system. Even though MSR plays an important role in software engineering research, few tools have been created and made public to support developers in extracting information from Git repository. In this paper, we present PyDriller, a Python Framework that eases the process of mining Git. We compare our tool against the state-of-the-art Python Framework GitPython, demonstrating that PyDriller can achieve the same results with, on average, 50% less LOC and significantly lower complexity.URL: https://github.com/ishepard/pydrillerMaterials: https://doi.org/10.5281/zenodo.1327363Pre-print: https://doi.org/10.5281/zenodo.1327411",
	author = "Spadini, Davide and Aniche, Maurício and Bacchelli, Alberto",
	year = "2018",
	doi = "10.1145/3236024.3264598",
	booktitle = "The 26th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)",
}