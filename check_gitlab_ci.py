import os

filename = '.gitlab-ci.yml'

with open(filename, 'r') as f:
    content = f.read()

assert(content == "stages:\n  - test\n  - post_status\n\nunittest:\n    stage: test\n    script:\n        - bash test.sh &> status.out\n    tags:\n        - demo-runner\n\nstatus:\n    stage: post_status\n    script:\n        - python post_status.py\n    tags:\n        - demo-runner\n    when: always"), 'You are not allowed to change the .gitlab-ci.yml file'