import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
import random
import time

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

url = 'http://los-cabos-food.ro/?p=' + str(random.randint(1,135))
print bcolors.WARNING + url + bcolors.ENDC
r = Render(url)
html = r.frame.toHtml()
text = r.frame.toPlainText()
#print unicode(text)

baseUrl = r.mainFrame().baseUrl();
print unicode(baseUrl)
i = 0
collection = r.mainFrame().findAllElements("a");
for element in collection:
	href = element.attribute("href")
	print unicode(href)
	url2 = str(href)
	if(url2!='#'):
		i = i + 1
		print bcolors.OKGREEN + str(i) + " > goto > "+url2 + bcolors.ENDC 
		r.mainFrame().load(QUrl(url2))
		#print r.mainFrame().loadFinished()
		secs = random.randint(1,3)
		time.sleep(secs)
		text = r.frame.toPlainText()
		#print unicode(text)
