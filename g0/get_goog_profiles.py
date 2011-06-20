#!/usr/bin/python

import urllib2
import re
import time
 
for i in range(1000, 9999):
	print i
	urlpagina = 'http://www.gstatic.com/s2/sitemaps/sitemap-' + str(i) + '.txt'
	savepagina = str(i) + '.txt'
	try :
		myFile = open(savepagina,'a')
		request = urllib2.Request(urlpagina)
		request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
		response = urllib2.urlopen(request)
		for line in response.read().split('\n'):
			myFile.write(line+'\n')
		myFile.close()
	except:
		pass
	

