#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type:text/html")
print("")


print("Success")
form= cgi.FieldStorage()
name = form.getvalue('cname')
size = form.getvalue('csize')
unit= form.getvalue('cunit')
client_ip = form.getvalue('clientip')
cloud_ip = form.getvalue('cloudip')

print(name+ " " + size+  " "+ unit + " " + client_ip )

staas_setup= sp.getstatusoutput("sudo ansible-playbook lv.yml --extra-vars='csize={} csizeunit={} drive={} clientip={}'".format(size,unit,name,client_ip))

if staas_setup[0]==0:
	print("Cloud has been set")


client_setup= sp.getstatusoutput("sudo ansible-playbook lv_client.yml --extra-vars='x={} y={}'".format(name,cloud_ip))

if client_setup[0]==0:
	print("\n client setup complete... Check Desktop to find theCloud Folder")

