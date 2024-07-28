import os

from git import Repo

from utils.helpers import (
    are_changes_uncommited,
    is_git_repo,
    try_fetch,
    update_repo
)
from utils.log import Log


PATH: str = "AiMusicBot"
SCRIPTS_PATH: str = "scripts"
YTP_PATH: str  = "ytp"
AI_REPO: str = "git@github.com:OesusDevelopmentStudios/AiMusicBot.git"
YTP_REPO: str = "git@github.com:OesusDevelopmentStudios/ytp.git"


def fetch_main(target: str) -> bool:
    if os.path.exists(target):
        Log.error("Folder " + PATH + " allready exists. Cannot fetch project!")
        return False
    os.makedirs(target)
    Log.info("Fetching main project...")
    Repo.clone_from(AI_REPO, target, branch="c++", progress=Log.log_progress)
    Log.info("\nDone")
    return True


def fetch_ytp(path: str) -> bool:
    target = os.path.join(path, YTP_PATH)
    if os.path.exists(target):
        Log.error("Folder " + target + " allready exists. Skiping fetching of subproject ytp")
        return False
    os.mkdir(target)
    Log.info("Fetching ytp dependency...")
    Repo.clone_from(YTP_REPO, target, progress=Log.log_progress)
    Log.info("\nDone")


def handle_fetch(path: str):
    project_dir = os.path.join(path, PATH)
    if not try_fetch(fetch_main, project_dir, "AiMusicBot"):
        return
    scripts_dir = os.path.join(project_dir, SCRIPTS_PATH)
    if not os.path.exists(scripts_dir):
        os.mkdir(scripts_dir)
    if not try_fetch(fetch_ytp, scripts_dir, "ytp"):
        return


def handle_build(path: str):
    if os.path.basename(path) != PATH:
        Log.error("Not a project root!")
        return
    os.system("make compile-release")
    os.chdir("scripts/ytp")
    os.system("python3 -m venv ./.venv")
    os.system(".venv/bin/pip3 install -r requirements.txt")


def handle_update(path: str):
    Log.info("Checking state...")
    if not is_git_repo(path):
        return
    if os.path.basename(path) != PATH:
        Log.error("Not a project root!")
        return
    if are_changes_uncommited(path, "AiMusicBot", branch="c++"):
        return
    ytp_path = os.path.join(path, SCRIPTS_PATH, YTP_PATH)
    if not is_git_repo(ytp_path):
        return
    if are_changes_uncommited(ytp_path, "ytp"):
        return

    update_repo(path, "main")
    update_repo(ytp_path, "ytp")


def ai_handle(cmd: str):
    current_path = os.getcwd()

    if cmd == "fetch":
        handle_fetch(current_path)
    elif cmd == "build":
        handle_build(current_path)
    elif cmd == "update":
        handle_update(current_path)
    else:
        print("Command unsupported for this project")
