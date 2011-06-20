#!/usr/bin/env python

import gtk
import webkit
import gobject
import random

for n in range(1,100):
	gobject.threads_init()
	win = gtk.Window()
	bro = webkit.WebView()
	i = random.randint(1, 125) 
	bro.open("http://los-cabos-food.ro/?p="+str(i))
	win.add(bro)
	win.show_all()

gtk.main()
