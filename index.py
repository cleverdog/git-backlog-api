import os
import git

_repo_path = os.path.join('./', 'repo')
# clone from remote
git_repo = git.Repo.clone_from('gitclb@gitclb.git.backlog.com:/TEST/test.git', _repo_path, branch='master')

# create future branch
origin = git_repo.remote()
git_repo.create_head('feature/my_new_branch')
origin.push('feature/my_new_branch')
