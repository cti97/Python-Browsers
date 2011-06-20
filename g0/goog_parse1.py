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

p_start = 10
p_end = 20

i=0
for arg in sys.argv: 
	i = i + 1
	print str(i) + " " + arg
	if (i==2): p_start = int(arg)
	if (i==3): p_end = int(arg)
 
for i in range(p_start, p_end):
	savepagina = 'google_profiles/' + str(i) + '.txt'
	print bcolors.WARNING + str(i) + " " + savepagina + bcolors.ENDC
	myFile = open(savepagina,'r')
	for line in myFile.read().split('\n'):
		urlpagina = line
		try :
			nume = ""; detalii = ""; linkuri = ""; body = ""
			request = urllib2.Request(urlpagina)
			request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
			response = urllib2.urlopen(request)
			for line2 in response.read().split('\n'):
				if line2.find('Sex')>0: 
					xxx = line2[line2.find('Sex'):line2.find('Sex')+60]
					xxx = xxx.replace('</h2><div class="a-d-y-z-hb c-t-s">',' ')
					yyy = xxx.split('</div>')
					detalii = detalii + "<p>" + yyy[0] + "</p>"
					xxx = bcolors.WARNING + yyy[0] + bcolors.ENDC
					print xxx

				if line2.find('Ocupaţie</h2><div class="a-d-y-z-hb c-t-s title">')>0: 
					xxx = line2
					xxx = line2[line2.find('Ocupaţie'):line2.find('Ocupaţie')+100]
					xxx = xxx.replace('</h2><div class="a-d-y-z-hb c-t-s title">',' ')
					yyy = xxx.split('</div>')
					detalii = detalii + "<p>" + yyy[0] + "</p>"
					xxx = bcolors.WARNING + yyy[0] + bcolors.ENDC
					print xxx

				xxx = ''
				if line2.find('<title>')>0: 
					xxx = line2[line2.find('<title>'):line2.find('</title>')]
					xxx = xxx.replace('<title>','')
					xxx = xxx.replace(' - Profil Google','')
					nume = xxx
					xxx = bcolors.HEADER + urlpagina + " " + bcolors.OKGREEN + xxx + bcolors.ENDC
				if line2.find('Linkuri')>0: 
					xxx = line2
					xxx = line2[line2.find('Linkuri'):line2.find("<script>window.jstiming.load.tick('aboutEnd');")]
					xxx = xxx.replace('</h2><ul class="a-d-y-z-Dg fe"><li>',' ')
					xxx = xxx.replace('</div>',' ')
					xxx = xxx.replace('</li></ul> ','')
					xxx = xxx.replace('<div class="a-d-y-i i"><a class="a-d-y-i-Ng url"','<a')
					xxx = xxx.replace('<img alt="" class="a-d-y-cf" src="/c/favicons?domain=picasaweb.google.com"/>','')
					xxx = xxx.replace('rel="me" target="_blank" title="Deschideţi acest link într-o filă nouă"','')
					xxx = xxx.replace('target="_blank" title="Deschideţi acest link într-o filă nouă"','')
					xxx = xxx.replace('alt="" class="a-d-y-cf"','')
					linkuri = "<ul><li>" + xxx + "</li></ul>"
				if xxx != "": print xxx
			
			body = "<h1>"+nume+"</h1>"+"<h2>Detalii</h2>"+detalii+"<h2>Linkuri</h2>"+linkuri
			putitin = 'http://catalist.ro/dev1_tsn/?backuser=borg&link='+urllib.quote(urlpagina)+'&title='+urllib.quote(nume)+'&body='+urllib.quote(body);
			#print putitin
			request2 = urllib2.Request(putitin)
			request2.add_header('UserAgent', 'Ruel.ME Sample Scraper')
			response2 = urllib2.urlopen(request2)
		except:
			pass
	myFile.close()

	

