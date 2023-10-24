import requests
from helpers.types import Selection, SelectionState


class GitOrca:
    """
    Git-Orca
    """
    def __init__(self, github_access_token: str = None):
        """
        Initialize git-orca with github access token
        """
        self.github_access_token = github_access_token

    def get_issues(self, repo_name: str, repo_owner: str, state: SelectionState = 'open', per_page: int = 20, page : int = 1):
        """
        Get issues
        """
        response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": f"Bearer {self.github_access_token}"
            },
            params={
                "state": f"{state}",
                "per_page": f"{per_page}",
                "page": f"{page}"
            }
        )
        return response.json()

    def get_prs(self, repo_name: str, repo_owner: str, state: SelectionState = 'open', per_page: int = 20, page : int = 1):
        """
        Get pull requests
        """
        response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": f"Bearer {self.github_access_token}"
            },
            params={
                "state": f"{state}",
                "per_page": f"{per_page}",
                "page": f"{page}"
            }
        )
        return response.json()
