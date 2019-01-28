Description:
This is a small project intended to report the changes in method signatures of
a Java repository. It uses the pydriller library for easy APIs into accessing
Git information such as commit hashes and diffs. It uses regex to determine if
a line is a method signature and as such is limited to when the signature is on
the same line and can not detect changes to parameters on different lines. It
also can not detect method signatures that have implicit access modifiers.

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
