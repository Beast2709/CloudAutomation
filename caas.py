#!/usr/bin/python36

print("content-type:text/html")
print("")


import subprocess as sp
import cgi 

#form = cgi.FieldStorage()
#data = form.getvalue('contname')

print("<form action='caas.py'>")
print("<br/>")
count=0
print("Enter the name of the container : ")
print("<input type='text' name='contname'>")
print("<br/>")
contain = "cont"+str(count)
sp.getoutput("sudo ansible-playbook caas.yml --extra-vars 'x={}'.format(contain)")
print ("<center><a href='http://192.168.43.86:4200' target='f1'>Click here to access Shell</a></center>")
print("<br/>")
print("<iframe name='f1' style='width:100%; height:100%;'></iframe>")
count=count+1
print("</form>")


