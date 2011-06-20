import shutil
import os
import time
import datetime
import math
import urllib2
import sys
import time

from array import array


myFile = open('ghiseul.html','a')
for i in range(100000001, 100008233):
	print i

	urlpagina = 'http://www.ghiseul.ro/ghiseul/public/plata/dovada/order/' + str(i)
	filehandle = urllib.urlopen(urlpagina) 
	print urlpagina
	
	myFile.write(urlpagina)
	
	for lines in filehandle.readlines():
		if lines.find('Serviciul este momentan indisponibil')!=1:
			myFile.write(lines)
	
	filehandle.close()
	time.sleep(2)
myFile.close()

