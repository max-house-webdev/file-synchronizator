from pathlib import Path


def set_local_dir_path(parent_dir: str = "") -> Path:
    """Set absolute path to local directory

    :param parent_dir: parent directory
    """
    LOCAL_DIR = "local_dir"

    if parent_dir == "" or \
            parent_dir.strip().lower() == "none":
        abs_path = Path.cwd().absolute()

    elif parent_dir.strip().lower() == "home":
        abs_path = Path.home().absolute()

    else:
        abs_path = Path.home().absolute().joinpath(parent_dir)

    return abs_path.joinpath(LOCAL_DIR)
