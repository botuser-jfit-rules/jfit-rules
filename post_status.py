import os
import github
import subprocess
import ftplib

sha = os.popen('git rev-parse HEAD').read().strip()
g = github.Github("ayushgithub", "Ayushman1")
session = ftplib.FTP('files.000webhost.com','ayushmansisodiya','Ayushman1')
session.cwd('public_html')

status_file = 'status.out'
with open(status_file, 'r') as f:
    description = f.read()
with open(status_file, 'r') as f:
    session.storbinary('STOR ' + sha + '.txt', f)

print description, len(description)
if len(description) != 0:
    state = 'failure'
    description = 'Some test[s] failed. Click to check details'
else:
    state = 'success'
    description = 'All test passed'

repo = g.get_repo('ayushgithub/jfit-rules')
commit = repo.get_commit(sha)

ret = commit.create_status(state=state, target_url='https://ayushmansisodiya.000webhostapp.com/'+sha+'.txt', description=description)
session.quit()
