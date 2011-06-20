import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *


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

for n in range(1, 50):
	try :
		url = 'dev1.the-socialnetwork.com'
		r = Render(url)	
		html = r.frame.toHtml()	
		print n
	except:
		pass	
	
