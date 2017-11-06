# -*- coding: ISO-8859-1  -*-
import csv
import re
import os
import sys
import codecs
import requests
koden=sys.stdin.encoding
print(sys.getdefaultencoding())
from random import randint
import random
import time

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

import urllib

driver = []

year = []
starter = []
a1 = []
a2 = []
a3 = []
peng = []
cells = []

bana = []
spar = []
distans = []
tid = []
start = []
hast = []
trainer = []
utstring= ''


d_path = 'Kuskdata/'
#d_file = '4401'

#f = open(d_path + d_file)

d_files = [h for h in listdir(d_path) if isfile(join(d_path, h))]
utfil = open('kuskdata','a')

for i in d_files:
	year = []
	starter = []
	a1 = []
	a2 = []
	a3 = []
	peng = []
	cells = []
	f = open(d_path + i)
	soup = BeautifulSoup(f.read(),"lxml")
	content = soup.find("div",{"id":"content"})
	h1 = content.find_all('h1')
	if len(h1) > 1:
		utstring = str(h1[1].text.encode('utf-8')) + '\t'
		tab = content.find('div',{'class':'tab-panel'})

		first = tab.find_all('table')

		for fir in first:
		#	print fir
			
			if 'Segerprocent' in str(fir):
	#			print "seger"
				trs = fir.find_all('tr')
				for t in trs:
					cells = t.find_all('td')
	#				print len(cells)
					if len(cells)>0:
						year.append(cells[0])
						starter.append(str(cells[1].text))
						a1.append(str(cells[2].text))
						a2.append(str(cells[3].text))
						a3.append(str(cells[4].text))
					#	peng.append(str(cells[6].text))
				
				for u in starter:
					utstring = utstring + u + '\t'
				for u in a1:
					utstring = utstring + u + '\t'
				for u in a2:
					utstring = utstring + u + '\t'
				for u in a3:
					utstring = utstring + u + '\t'
			#	for u in peng:
			#		utstring = utstring + u + '\t'
						
				
				print utstring 
				utfil.write(utstring + '\n')
	f.close()		
utfil.close()
