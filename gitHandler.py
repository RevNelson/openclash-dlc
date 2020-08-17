import subprocess

repo_base = "./dlc"


def fetch_submodule():
    try:
        fetch = subprocess.Popen(
            ['git', 'submodule', 'update', '--init', '--recursive'])
        fetch.wait()
        return ("Git submodule loaded.\n")
    except Exception as err:
        return err


def pull_repo():
    print("Pulling latest commit from git...")
    try:
        pull = subprocess.Popen(
            ['git', 'pull', '-v', 'origin', 'master'], cwd=repo_base)
        pull.wait()
        return ("Git pull successful.\n")
    except Exception as err:
        return err
