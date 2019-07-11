#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import os
from collections import OrderedDict

def run_command(key, command, ssh):
    (stdin, stdout, stderr) = ssh.exec_command(command)
    for line in stdout.readlines():
        print key + " " + line.rstrip("\n\r")

ip = ""
username = ""

commands = OrderedDict()

commands['CurrentTime'] = 'date'
commands['Hw'] = 'echo HelloWorld'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)

ssh.connect(ip, 22, username, pkey = mykey)

for key, value in commands.items():
    run_command(key, value, ssh)
    print "---"

ssh.close()
