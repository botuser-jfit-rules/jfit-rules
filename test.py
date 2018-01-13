import os
from subprocess import Popen, PIPE
import sys
import github

g = github.Github("ayushgithub", "Ayushman1")
sha = os.environ.get('ghprbActualCommit')
pullid = os.environ.get('ghprbPullId')
repo = g.get_repo('ayushgithub/jfit-rules')
pull_request = repo.get_pull(int(pullid))
commit = repo.get_commit(sha)

test_folder = 'rules'
exit_code = 0
rules = os.listdir(test_folder)

for rule in rules:
    testfile_path = os.path.join(test_folder, rule)
    p = Popen(['bash','validate.sh',testfile_path], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print p.returncode, output, error
    if p.returncode != 0:
        exit_code = p.returncode
        print rule,'failed'
        pull_request.create_review_comment(body=error, commit_id=commit, path=os.path.join(test_folder,rule), position=1)

if exit_code != 0:
    sys.exit(exit_code)