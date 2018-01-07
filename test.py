import os
from subprocess import Popen, PIPE
import sys

outfile = 'status.out'
test_folder = 'rules'
test_flag = True

rules = os.listdir(test_folder)

with open(outfile, 'a') as f:
    for rule in rules:
        testfile_path = os.path.join(test_folder, rule)
        p = Popen(['python',testfile_path], stdout=PIPE, stderr=PIPE)
        output, error = p.communicate()
        # print p.returncode, output, error
        if p.returncode != 0:
            f.write(rule + ' failed\n')
            test_flag = False

# print test_flag
if test_flag == False:
    sys.exit('Some test failed. Check status.out')
