```python
import git
from git import Repo

class GitDeployment:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = Repo(self.repo_path)

    def git_push(self):
        try:
            self.repo.git.add(update=True)
            self.repo.index.commit("Automated commit by ChatGPT")
            origin = self.repo.remote(name='origin')
            origin.push()
        except:
            print('Some error occured while pushing the code')

    def git_pull(self):
        try:
            self.repo.git.pull()
        except:
            print('Some error occured while pulling the code')

    def git_clone(self, git_url, clone_directory):
        try:
            git.Git(clone_directory).clone(git_url)
        except:
            print('Some error occured while cloning the repository')
```
