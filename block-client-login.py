#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type:text/html")
print("")
form= cgi.FieldStorage()
cloud_ip = form.getvalue('cloudip')
client_setup= sp.getstatusoutput("sudo ansible-playbook block-client-login.yml --extra-vars='ip={}'".format(cloud_ip))
if client_setup[0]==0:
        print("You are logged in..")


