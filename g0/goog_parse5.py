#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import time
import sys
import codecs

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

p_start = 10
p_end = 20

#i=0; 
#for arg in sys.argv: 
#	i = i + 1
#	if (i==2): p_start = int(arg)
#	if (i==3): p_end = int(arg)
fnrord = open("nrord.txt",'r')
line = fnrord.read()
print line
p_start = int(line)
p_end = p_start + 10
fnrord.close()

fnrord = open("nrord.txt",'w')
fnrord.write(str(p_end))
fnrord.close()

for i in range(p_start, p_end):
	j=0;
	savepagina = 'google_profiles/' + str(i) + '.txt'
	print bcolors.WARNING + str(i) + " " + savepagina + bcolors.ENDC
	myFile = open(savepagina,'r')
	#myFile2 = open('sql/'+str(i)+'.sql','a')
	myFile2 = codecs.open('sql/'+str(i)+'.sql', 'wt', 'utf-8')
	for line in myFile.read().split('\n'):
		urlpagina = line
		try :
			nume = ""; detalii = ""; linkuri = ""; body = ""; j = j + 1
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
					xxx = bcolors.FAIL + str(i) + " // " + str(j) + ": " + bcolors.HEADER + urlpagina.replace('https://profiles.google.com','') + " " + bcolors.OKGREEN + xxx + bcolors.ENDC
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
					xxx = xxx.replace('src="/c/favicons','src="https://profiles.google.com/c/favicons')	


					body = xxx
					xxx = ""
				if xxx != "": print xxx

			sqlsave = "INSERT INTO wp_posts (post_date, post_title, post_content, post_author) VALUES ('2011-05-20 17:49:01','"+nume+"','"+body+"<br/>Source: "+'<a href="'+urlpagina+'">'+nume+' Google Profile</a>'+"',1);"
			sqlsave = sqlsave.replace("\',","',")
			sqlsave = sqlsave.replace("\')","')")
			myFile2.write(sqlsave+'\n')

			#putitin = 'http://dev1.the-socialnetwork.com/?backuser=borg&link='+urllib.quote(urlpagina)+'&title='+urllib.quote(nume)+'&body='+urllib.quote(body);
			#print putitin
			#request2 = urllib2.Request(putitin)
			#request2.add_header('UserAgent', 'Ruel.ME Sample Scraper')
			#response2 = urllib2.urlopen(request2)
		except:
			pass
	myFile.close()
	myFile2.close()


	

