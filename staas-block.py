#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type:text/html")
print("")


form= cgi.FieldStorage()
name = form.getvalue('cname')
size = form.getvalue('csize')
unit= form.getvalue('cunit')


staas_setup= sp.getstatusoutput("sudo ansible-playbook block-cloud.yml --extra-vars='csize={} csizeunit={} cloud={}'".format(size,unit,name))
if staas_setup[0]==0:
        print("Cloud has been set")
print("""
<form action='block-client-login.py'>
<table >
<tr>
</br>
<td> Enter cloud ip: </td>
<td> <input required pattern= "^([0-9]{1,3}\.){3}[0-9]{1,3}$" name='cloudip'
</tr>
<tr>
<td> <button type="submit"> Login </button> </td>
</tr>
</table>
</form>
<form action='block-client-logout.py'>
<table >
<tr>
</br>
<td> Enter cloud ip: </td>
<td> <input required pattern= "^([0-9]{1,3}\.){3}[0-9]{1,3}$" name='cloudip'
</tr>
<tr>
<td> <button type="submit"> Logout </button> </td>
</tr>
</table>
</form>
""")
