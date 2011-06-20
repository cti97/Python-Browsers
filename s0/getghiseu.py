#!/usr/bin/python

import urllib2
import re
import time
 
myFile = open('ghiseul.html','a')
for i in range(100000001, 100008233):
	print i
	urlpagina = 'http://www.ghiseul.ro/ghiseul/public/plata/dovada/order/' + str(i)
	try :
		request = urllib2.Request(urlpagina)
		request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
		response = urllib2.urlopen(request)
		for line in response.read().split('\n'):
			myFile.write(line)
	except:
		pass
	
myFile.close()
