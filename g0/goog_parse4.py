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

i=0
for arg in sys.argv: 
	i = i + 1
	if (i==2): urlpagina = arg

try :
	nume = ""; detalii = ""; linkuri = ""; body = ""

	request = urllib2.Request(urlpagina)
	request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
	response = urllib2.urlopen(request)

	for line2 in response.read().split('\n'):
		xxx = ''
		if line2.find('<title>')>0: 
			xxx = line2[line2.find('<title>'):line2.find('</title>')]
			xxx = xxx.replace('<title>','')
			xxx = xxx.replace(' - Profil Google','')
			nume = xxx
			xxx = bcolors.HEADER + urlpagina + " " + bcolors.OKGREEN + xxx + bcolors.ENDC
		if line2.find('<span class="fn">'+nume)>0: 
			xxx = line2[line2.find('<span class="fn">'+nume):line2.find("<script>window.jstiming.load.tick('aboutEnd');</script>")]
			xxx = xxx.replace('visibility:hidden;','')
			xxx = xxx.replace('height:200px;','')
			xxx = xxx.replace('<span role="button" class="c-i a-b-Z-Bc-ib-i a-d-fa-Bc-ib-i" title="Raportaţi un abuz" tabindex="0">Raportaţi acest profil</span>','')
			xxx = xxx.replace('<div class="c-la-qa">Buzz</div>','')
			xxx = xxx.replace('<div class="c-la-qa-Zm">Buzz</div>','')
			xxx = xxx.replace('<div class="c-la-qa">Despre</div>','')
			xxx = xxx.replace('<div class="c-la-qa-Zm">Despre</div>','')
			xxx = xxx.replace('<h2 class="a-d-y-z-Q c-t-s">Acasă</h2>','')
			xxx = xxx.replace('signature=','somethingelse=')
			xxx = xxx.replace('&amp;','&')
			xxx = xxx.replace('size=195x150','size=500x350')	
			xxx = xxx.replace('//maps-api-ssl.google.com/maps/api','http://maps.google.com/maps/api')	
			xxx = xxx.replace('%7C','|')	
			xxx = xxx.replace('&client=google-profiles','')	
			body = xxx
		if xxx != "": print xxx
except:
	pass
putitin = 'http://dev1.the-socialnetwork.com/?backuser=borg&link='+urllib.quote(urlpagina)+'&title='+urllib.quote(nume)+'&body='+urllib.quote(body);
#print putitin
request = urllib2.Request(putitin)
request.add_header('UserAgent', 'Ruel.ME Sample Scraper')
response = urllib2.urlopen(request)


	

