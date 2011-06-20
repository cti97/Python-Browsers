#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import time
import sys

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

j=0;i=0
print "begin"	
lasturl = ""
savepagina = '2_biertijd.html'
myFile = open(savepagina,'r')
myFile2 = open('sql/youtube.sql','a')
for line in myFile.read().split('\n'):
	urlpagina = line.replace('youtube.com/v/','www.youtube.com/watch?v=')
	urlsave = line.replace('http://youtube.com/v/','http://www.youtube.com/embed/')
	#print urlpagina
	i = i + 1
	nume = ""; detalii = ""; linkuri = ""; body = ""; j = j + 1
	try:
		request = urllib2.Request(urlpagina)
		request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
		response = urllib2.urlopen(request)
		for line2 in response.read().split('\n'):
			#print line2
			if line2.find("document.title = 'YouTube - ' + ")>0: 
				xxx = line2
				xxx = xxx.replace("document.title = 'YouTube - ' + ",'')
				xxx = xxx.replace('";','')
				xxx = xxx.replace('"','')
		#		print xxx
				nume = xxx.replace("'","`")
		#		print nume
		if (lasturl != urlpagina):
			print bcolors.WARNING + str(i) + " " + bcolors.HEADER + urlpagina + bcolors.OKGREEN + nume + bcolors.ENDC
			#putitin = 'http://video.catalist.ro/?backuser=youtube&link='+urllib.quote(urlpagina)+'&title='+urllib.quote(nume)+'&body='+urllib.quote(body);
			#print putitin
			lasturl = urlpagina
			body = '<iframe width="950" height="750" src="'+urlsave+'?hd=1" frameborder="0" allowfullscreen></iframe>'
			sqlsave = "INSERT INTO wp_posts (post_date, post_title, post_content, post_author) VALUES ('2011-05-24 20:49:01','"+nume+"','"+body+"<br/>Source: "+urlpagina+"',1);"
			#print sqlsave
			myFile2.write(sqlsave+'\n')
	except:
		pass
myFile.close()
myFile2.close()
print "end"		


	

