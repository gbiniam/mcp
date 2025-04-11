def get_latest_error(logfile="logs/error.log"):
    with open(logfile, "r") as f:
        lines = f.readlines()
        return lines[-1] if lines else "No logs found."
