#!/usr/bin/env python

import gtk
import webkit
import gobject
import random
import sys

i=0
for arg in sys.argv: 
	i = i + 1
	print str(i) + " " + arg
	if ((i==2) and (arg == 'cti97')): urldo = 'cti97'
	if ((i==2) and (arg == 'loscabos')): urldo = 'loscabos'
	if ((i==2) and (arg == 'dev1')): urldo = 'dev1'

for i in range(1,33):
	if (urldo=='cti97'): url = 'http://cti97.wordpress.com/?p=' + str(random.randint(1,26000))
	if (urldo=='loscabos'): url = 'http://los-cabos-food.ro/?p=' + str(random.randint(1,150))
	if (urldo=='dev'): url = 'http://dev1.the-socialnetwork.com/?p=' + str(random.randint(1,450000))
	gobject.threads_init()
	win = gtk.Window()
	bro = webkit.WebView()
	bro.open(url)
	win.add(bro)
	win.show_all()
 
gtk.main()
