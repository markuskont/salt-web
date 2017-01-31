#!/usr/bin/env python

import socket
import yaml
import subprocess

hostname = socket.gethostname()
grains = {
    'roles': [ 'abix' ]
}
command = ['service', 'salt-minion', 'restart']

if 'web-' in hostname:
    grains['roles'].append('web')
    
if 'db-' in hostname:
    grains['roles'].append('database')

with open('/etc/salt/grains', 'w') as outfile:
    yaml.dump(grains, outfile, default_flow_style=False)

subprocess.call(command, shell=False)
