# coding: utf-8
import os
import io
import time
import git
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/create-branch', methods=['POST'])
def post_json():
    content = request.json
    issue_type = content['content']['issueType']['name']
    key_id = content['content']['key_id']
    project_key = content['project']['projectKey']
    cat = 'OTHER'
    if issue_type == "タスク":
        cat = 'TASK'
    elif issue_type == "バグ":
        cat = 'BUG'
    elif issue_type == "要望":
        cat = 'REQUEST'
    branch_name = 'feature/' + project_key + '_' + cat + '_' + str(key_id)
    _repo_path = os.path.join('./', 'repo')
    # clone from remote
    git_repo = git.Repo.clone_from('gitclb@gitclb.git.backlog.com:/TEST/test.git', _repo_path, branch='master')
    # create future branch
    # origin = git_repo.remote()
    # git_repo.create_head(branch_name)
    # origin.push(branch_name)
    # os.system('rm -rf ' + _repo_path) 
    return branch_name

@app.route('/show-data', methods=['POST'])
def show_json():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))