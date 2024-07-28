class Log:
    def info(msg: str) -> None:
        print(msg)

    def warn(msg: str) -> None:
        print("WARNING: " + msg)

    def error(msg: str) -> None:
        print("ERROR: " + msg, flush=True)

    def log_progress(x, y, z, msg):
        if msg != "":
            print("\r" + msg, end="    ", flush=True)
