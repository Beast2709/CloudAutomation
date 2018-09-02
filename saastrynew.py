#!/usr/bin/python36

print("Content-Type:text/html")
print("\n")

import os,subprocess as sp
import cgi


c1=sp.getoutput("sudo ansible-playbook saasfirefox.yml")
print("<H1><center>Double Click 'ad.sh' on your Desktop to access the software</center></H1>")
