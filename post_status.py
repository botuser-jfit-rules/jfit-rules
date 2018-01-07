import os
import github
import subprocess

sha = os.popen('git rev-parse HEAD').read().strip()
g = github.Github("ayushgithub", "Ayushman1")

status_file = 'status.out'
with open(status_file, 'r') as f:
    description = f.read()
print description, len(description)
if len(description) != 0:
    state = 'failure'
    description = 'Some test[s] failed. Check details'
else:
    state = 'success'
    description = 'All test passed'

repo = g.get_repo('ayushgithub/jfit-rules')
commit = repo.get_commit(sha)

ret = commit.create_status(state=state, target_url="https://www.google.com", description=description)
