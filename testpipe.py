import sys
import os
import requests
import time
import json

servers = ['10.52.208.20','10.52.208.21']

for ip in servers:
    
  print ip  
  #Check Tomcat Process
  def checkTomcatProcess():
	  global processId
	  print 'checkTomcatProcess()'
    
  #Check Testconnection
  def checkTestConnection():
	  global processId	
	  print 'checkTestConnection()'

  #Check Tomcat Stopped
  def checkTomcatStopped():
	print 'checkTomcatStopped()'
	checkTestConnection()
		  
  checkTomcatProcess()
  checkTomcatStopped()

print 'exit'