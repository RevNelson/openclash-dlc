import subprocess

repo_base = "./dlc"


def pull_this_repo():
    print("Pulling latest Parser commit from git...")
    try:
        pull = subprocess.Popen(
            ['git', 'pull', '-v', 'origin', 'master'])
        pull.wait()
        return "openclash-dlc git pull successful.\n"
    except Exception as err:
        return err


def fetch_submodule():
    print("Ensuring submodule is linked and updated...")
    try:
        fetch = subprocess.Popen(
            ['git', 'submodule', 'update', '--init', '--recursive'])
        fetch.wait()
        return "Git submodule loaded.\n"
    except Exception as err:
        return err


def pull_dlc_repo():
    print("Pulling latest DLC commit from git...")
    try:
        pull = subprocess.Popen(
            ['git', 'pull', '-v', 'origin', 'master'], cwd=repo_base)
        pull.wait()
        return "DLC git pull successful.\n"
    except Exception as err:
        return err
