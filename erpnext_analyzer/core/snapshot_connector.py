import subprocess

class SnapshotConnector:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def get_latest_commit(self):
        """Captures the current Git state to 'tag' the snapshot."""
        try:
            cmd = ["git", "-C", self.repo_path, "rev-parse", "HEAD"]
            return subprocess.check_output(cmd).decode('ascii').strip()
        except:
            return "non-git-repo"

    def get_file_last_modified(self, rel_path):
        """Tells the AI how 'fresh' this specific logic is."""
        try:
            cmd = ["git", "-C", self.repo_path, "log", "-1", "--format=%cd", "--", rel_path]
            return subprocess.check_output(cmd).decode('ascii').strip()
        except:
            return "unknown"