#!/usr/bin/python

import urllib2
import re
import time
 
myFile = open('2_biertijd.html','a')
for i in range(1, 26000):
	print i
	urlpagina = 'http://biertijd.com/mediaplayer/?itemid=' + str(i)
	try :
		request = urllib2.Request(urlpagina)
		request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
		response = urllib2.urlopen(request)
		for line in response.read().split('\n'):
			if line.find('Institutie:')>0: 
				xxx = line[line.find('Institutie:'):line.find('Institutie:')+30]
				print str(i) + ': ' + xxx
				myFile.write('http://'+xxx+'\n')
	except:
		pass
	
