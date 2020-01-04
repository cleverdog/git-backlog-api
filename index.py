import os
import git

_repo_path = os.path.join('./', 'repo')
# clone from remote
ssh_executable = '../ssh_cmd'
git_repo = git.Repo.clone_from('gitclb@gitclb.git.backlog.com:/TEST/test.git', _repo_path, branch='master').git.custom_environment(GIT_SSH=ssh_executable)
# git_repo = git.Repo.clone_from('gitclb@gitclb.git.backlog.com:/TEST/test.git', _repo_path, branch='master')

# create future branch
origin = git_repo.remote()
git_repo.create_head('feature/my_new_branch')
origin.push('feature/my_new_branch')
