import subprocess

repo_base = "./dlc"


def pull_repo():
    print("Pulling latest commit from git...")
    try:
        pull = subprocess.Popen(
            ['git', 'pull', '-v', 'origin', 'master'], cwd=repo_base)
        pull.wait()
        return ("Git pull successful.\n")
    except Exception as err:
        return err
