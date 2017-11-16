#!/usr/bin/python

from pybrain.tools.xml.networkreader import NetworkReader
import sys 
import cgi, cgitb 
print "Content-type:text/html\r\n\r\n"
form = cgi.FieldStorage() 
data=list()
i=0
while i<784:
	data.append(form.getvalue('data['+str(i)+']'))
	i=i+1

net=NetworkReader.readFrom('net1.xml')
a= net.activate(data)
max = a[0]
pos = 0
for i in range(len(a)):
    if a[i]>max: max=a[i];pos=i
print pos