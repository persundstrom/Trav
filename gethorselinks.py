# -*- coding: utf-8  -*-

import random
import time
import csv
import ftfy
import os
import sys
import codecs
import requests
koden=sys.stdin.encoding
print(sys.getdefaultencoding())
#import numpy as np
os.system("chcp 1252")
import os.path
from bs4 import BeautifulSoup
import urllib

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join, exists
#mypath = 'home/per/Dropbox/iMacros/Downloads/testhorse/'
mypath = 'C:/Users/Per/Dropbox/Trav/raceday/'
mypathras = 'C:/Users/Per/Dropbox/Trav/'

f=open(mypath + 'race.txt','r',encoding='utf8')
fout=open(mypathras + 'horselinks.txt','a',encoding='utf8')
urls = f.read()
lines = urls.split('\n')
print (lines)
cnt=0
for line in lines:
	page = urllib.request.urlopen(line).read()
	soup = BeautifulSoup(page,'lxml')
	#print(soup.prettify())
	tab = soup.find('table',{'id':'myTable'})
	cnt=cnt+1
	print('cnt   ' + str(cnt))
	if tab != None:
		link = tab.find_all('a', href=True)
		for l in link:
		#	print(l['href'])
			if 'hast' in l['href']:
				fout.write(l['href'] + '\n')
				print(l['href'])
#	row = soup.find('td',{'id':'id3'}).parent					
	#if row != None:
	#	print (row.prettify())
#	tds=row.find_all('td')
#	print (len(tds))
#	for td in tds:
#		print (td.text)
#	fras.write(str(tds[3].text) + '\n')
#	aind = str(tds[4].text).split(' ')
#	if tds[5].text != '':
#		fout.write(span.text + '\t' + str(tds[0].text) + '\t' + str(tds[1].text) + '\t' + str(tds[2].text) + '\t' + str(tds[3].text) + '\t' + aind[0] + '\t' + aind[1].replace(',','.') + '\t' + str(tds[5].text).replace(',','.') + '\n')
	time.sleep(random.randint(1, 4))
f.close()
#fras.close()
fout.close()
