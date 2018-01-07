import os
from subprocess import Popen, PIPE
import sys

outfile = 'status.out'
test_folder = 'rules'

rules = os.listdir(test_folder)

open(outfile, 'w').close()
with open(outfile, 'a') as f:
    for rule in rules:
        testfile_path = os.path.join(test_folder, rule)
        p = Popen(['python',testfile_path], stdout=PIPE, stderr=PIPE)
        output, error = p.communicate()
        # print p.returncode, output, error
        if p.returncode != 0:
            f.write(rule + ' failed\n')
