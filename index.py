import os
import git

# SSH鍵の書き出し
with open('./id_rsa.pub', 'w') as f:
    f.write('<SSH Key>')
    os.chmod('./id_rsa.pub', 0o600)
# SSHコマンドの書き出し
with open('./ssh_cmd', 'w') as f:
    f.write('ssh -i ../id_rsa.pub -oIdentitiesOnly=yes "$@"')
    os.chmod('./ssh_cmd', 0o777)

_repo_path = os.path.join('./', 'repo')
# clone from remote
git_repo = git.Repo.clone_from('gitclb@gitclb.git.backlog.com:/TEST/test.git', _repo_path, branch='master')

# create future branch
origin = git_repo.remote()
git_repo.create_head('feature/my_new_branch')
origin.push('feature/my_new_branch')
