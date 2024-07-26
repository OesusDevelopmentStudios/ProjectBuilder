import os

from git import Repo

from utils.log import Log


PATH = "AiMusicBot"
AI_REPO = "git@github.com:OesusDevelopmentStudios/AiMusicBot.git"



def handle_fetch(path: str):
    target = os.path.join(path, PATH)
    if os.path.exists(target):
        Log.error("Folder " + PATH + " allready exists. Cannot fetch project!")
        return
    os.makedirs(target)
    Log.info("Fetching main project...")
    Repo.clone_from(AI_REPO, target, branch="c++", progress=Log.log_progress)
    Log.info("\nDone")

def handle_build():
    print("TODO")


def handle_update():
    print("TODO")


def ai_handle(cmd: str):
    current_path = os.getcwd()

    if cmd == "fetch":
        handle_fetch(current_path)
    elif cmd == "build":
        handle_build()
    elif cmd == "update":
        handle_update()
    else:
        print("Command unsupported for this project")
