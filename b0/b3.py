import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import random

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

app = QApplication(sys.argv)

def convertIt2():
	#web.print_(printer)
	x = ''
def convertIt():
	#web.print_(printer)
	print "Done "
	#QApplication.exit()
	x = web.mainFrame().toPlainText()
	print unicode(x)
	i = 0
	collection = web.mainFrame().findAllElements("a");
	for element in collection:
		href = element.attribute("href")
		#print unicode(href)
		url2 = str(href)
		if(url2!='#'):
			if (url2!='http://los-cabos-food.ro'):
				i = i + 1
				print bcolors.OKGREEN + str(i) + " > goto > "+url2 + bcolors.ENDC 
				web.mainFrame().load(QUrl(url2))
				QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt2)
				#text = web.frame.toPlainText()
				#print unicode(text)

url = 'http://los-cabos-food.ro/?p=' + str(random.randint(1,135))
web = QWebPage()
web.mainFrame().load(QUrl(url))

QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

#x = web.mainFrame().toPlainText()
#print x

sys.exit(app.exec_())
