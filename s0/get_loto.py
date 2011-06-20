#!/usr/bin/python

import urllib2
import re
import time
 
myFile = open('loto_result_2011.html','w')

urlpagina = 'http://loto.ro/index.php/649/rezultate.html?showall=1' 

request = urllib2.Request(urlpagina)
request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
response = urllib2.urlopen(request)
for line in response.read().split('\n'):
	sw = 0
	sss = ''
	if line.find('date-castig')>0: 
		sw = 1
	if line.find('numbers-castig')>0:
		sw = 1
	if sw:
		xxx = line.replace('<h3 id="numbers-castig">','')
		xxx = xxx.replace('</h3>','')
		xxx = xxx.replace('</h2>','')
		xxx = xxx.replace('<h2 id="date-castig">','')
		if len(xxx) > 3:
			myFile.write(sss+'\n')
		else:
			sss = sss & xxx;

	
