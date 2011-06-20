#!/usr/bin/python

import urllib2
import re
import time
 
myFile = open('ghiseul.html','a')
for i in range(100000001, 100008235):
	print i
	urlpagina = 'http://www.ghiseul.ro/ghiseul/public/plata/dovada/order/' + str(i)
	try :
		request = urllib2.Request(urlpagina)
		request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
		response = urllib2.urlopen(request)
		for line in response.read().split('\n'):
			if line.find('Institutie:')>0: 
				print str(i) + ': ' + line
				myFile.write(line+'\n')
			if line.find('Numar dovada de plata')>0: 
				print str(i) + ': ' + line
				myFile.write(line+'\n')
			if line.find('Data platii')>0: 
				print str(i) + ': ' + line
				myFile.write(line+'\n')
			if line.find('Valoare')>0: 
				print str(i) + ': ' + line
				myFile.write(line+'\n')
			if line.find('Comision')>0: 
				print str(i) + ': ' + line
				myFile.write(line+'\n')
			if line.find('Total valoare')>0: 
				print str(i) + ': ' + line
				myFile.write(line+'\n')
			if line.find('Contribuabil')>0: 
				print str(i) + ': ' + line
				myFile.write(line+'\n')
			if line.find('CNP/CUI')>0: 
				print str(i) + ': ' + line
				myFile.write(line+'\n')
	except:
		pass
	
myFile.close()
