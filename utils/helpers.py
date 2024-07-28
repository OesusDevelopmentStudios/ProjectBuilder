from git import Repo, exc
from typing import Callable

from utils.log import Log


def try_fetch(target: Callable, arg: str, name: str) -> bool:
    try:
        return target(arg)
    except:
        Log.error("Failed to fetch " + name)
        exit(500)


def is_git_repo(path: str) -> bool:
    try:
        _ = Repo(path).git_dir
        return True
    except exc.InvalidGitRepositoryError:
        Log.error("Path " + path + " is not a git repository!")
        return False


def are_changes_uncommited(path: str, name: str, branch: str="master") -> bool:
    repo = Repo(path)
    diff = repo.git.diff()
    if diff != "":
        Log.error(name + " has uncommited changes!")
        return True
    staged_diff = repo.index.diff("HEAD")
    if staged_diff:
        Log.error(name + " has uncommited changes!")
        return True
    repo.git.fetch()
    branch_diff = list(repo.iter_commits(branch + '@{u}..' + branch))
    if branch_diff:
        Log.error(name + " has unpushed changes!")
        return True
    return False


def update_repo(path: str, name: str):
    Log.info("Updating " + name + "...")
    repo = Repo(path)
    result = repo.git.pull()
    print(result)
