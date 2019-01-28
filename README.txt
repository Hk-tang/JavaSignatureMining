Description:
This is a small project intended to report the changes in method signatures of
a Java repository. It uses the pydriller library for easy APIs into accessing
Git information such as commit hashes and diffs and regex to match signatures.

Limitations:
1) The program uses regex instead of a parser to determine if a line is a method
signature, as such it can not recognize signatures where the parameters are on
different lines because the program reads the Git changes line by line and the
entire signature is split between different lines.
2) The regex also explicitly looks for access modifiers and can not recognize
methods with implicit access modifiers.
3) The program can not differentiate between overloaded methods and will output
false positives to the results file

Installation:
This project requires Python3 and Pydriller

Please read the official Python documentation to install Python properly
(This project uses Python 3.6.7)
    https://www.python.org/downloads/

To install pydriller you need to have pip installed and run:
    pip install pydriller

Usage:
Run the program using Python and provide paths to the Git repositories you want
to analyze. ex. python3 reader.py repo1 repo2 ...

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
