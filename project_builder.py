#!.venv/bin/python3

import argparse
import os
import sys
import git

from utils.custom_formatter import CustomFormatter
from src.ai_music_bot import ai_handle


PROJECTS: list[str] = ["ai_music_bot" ,"prolog"]
OPERATIONS: list[str] = ["fetch", "build", "test", "update"]

SUPPORTED_OPERATIONS: str \
    = "\nfetch  - Clones the projest and all required files (Requires project)" \
    + "\nbuild  - Builds the test binary (Requires project)" \
    + "\ntest   - Builds the test binary (if not build already) and launches all tests (Requires project)" \
    + "\nupdate - Updates target project. If no argument given will update self"

OPERATION_MESSAGE: str = "[MANDATORY] Specifies what operation will be used. Currently supported are:" \
    + SUPPORTED_OPERATIONS
PROJECT_MESSAGE: str = "[OPTIONAL] Specifies what projest is going to be used. Currently supported are:"
for x in PROJECTS: PROJECT_MESSAGE = PROJECT_MESSAGE + "\n\t" + x


parser = argparse.ArgumentParser(
    prog="ProjectBuilder",
    description="Utility designed to make building and resolving dependencies for OesusDevelopmentStudios projects. \
                 Mainly designed to make development and testing easier.",
    formatter_class=CustomFormatter)
parser.add_argument("operation", help=OPERATION_MESSAGE)
parser.add_argument("project", nargs='?', help=PROJECT_MESSAGE)


def update_self() -> int:
    self_location = os.path.dirname(__file__)
    repo = git.cmd.Git(self_location)
    repo.fetch()
    out = repo.pull()
    print(out)
    return 0


def main(args: list[str]) -> int:
    operation = args.operation
    if operation not in OPERATIONS:
        print("Operation %s not supported!" % (operation))
        print("\nSupported operations are: " + SUPPORTED_OPERATIONS)
        return 1

    project: str = args.project
    if project is None:
        if operation == "update":
            return update_self()
        else:
            print("Missing target!")
            print("\nSupported projects are: " + str(PROJECTS))
            return 2

    if project == "prolog":
        print("TODO: Handle prolog")
        return 0
    if project == "ai_music_bot":
        ai_handle(operation)
        return 0
    else:
        print("Project %s not supported!" % (project))
        print("\nSupported projects are: " + str(PROJECTS))
        return 1

    return 3


if __name__ == '__main__':
    sys.exit(main(parser.parse_args()))
