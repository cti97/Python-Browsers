#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import random
import unicodedata

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

class Render(QWebPage):
	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self._loadFinished)
		
		self.mainFrame().load(QUrl(url))
		self.app.exec_()

	def _loadFinished(self, result):
		self.frame = self.mainFrame()
		self.app.quit()

url = 'http://dev1.the-socialnetwork.com/' + str(random.randint(1,400000))
print bcolors.OKGREEN + url + bcolors.ENDC
r = Render(url)
html = r.frame.toHtml().toUtf8()

for line2 in html.split('\n'):
	line = str(line2)
	print line
	if line.find('<title>')>0: 
		print bcolors.HEADER + line + bcolors.ENDC
#html2 = r.frame.toPlainText()
#print bcolors.HEADER + unicode(html2) + bcolors.ENDC

