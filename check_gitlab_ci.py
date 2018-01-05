import os

filename = '.gitlab-ci.yml'

with open(filename, 'r') as f:
    content = f.read()

assert(content == 'stages:\n  - test\n\nunittest:\n    stage: test\n    script:\n        - bash test.sh\n    tags:\n        - demo-runner'), 'You are not allowed to change the .gitlab-ci.yml file'