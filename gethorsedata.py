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
mypath = 'C:/Users/Per/Dropbox/Trav/horse/'
mypathras = 'C:/Users/Per/Dropbox/Trav/'

#f=open(mypath + 'horses.txt','r',encoding='utf8')

fout=open(mypathras + 'out.txt','a',encoding='utf8')

#lines = urls.split('\n')
#print (lines)

fin=open(mypathras + 'horselinks - Copy.txt','r',encoding='utf8')
urls = fin.read()
lines = urls.split('\n')
havegot =''
for line in lines:
	f=open(mypath + 'horses.txt','r',encoding='utf8')		
	havegot = f.read()
	f.close()
	if line not in havegot:
		page = urllib.request.urlopen(line).read()
		soup = BeautifulSoup(page,'lxml')
		#print(soup.prettify())
		cont = soup.find('div',{'id':'content'})
		if cont != None:
			h1 = cont.find_all('h1')
			span = h1[1].find('span')
			print(span.text)
				
		row = soup.find('td',{'id':'id3'}).parent					
		#if row != None:
		#	print (row.prettify())
		tds=row.find_all('td')
		print (len(tds))
		for td in tds:
			print (td.text)
		aind = str(tds[4].text).split(' ')
		if tds[5].text != '':
			fout.write(span.text + '\t' + str(tds[0].text) + '\t' + str(tds[1].text) + '\t' + str(tds[2].text) + '\t' + str(tds[3].text) + '\t' + aind[0] + '\t' + aind[1].replace(',','.') + '\t' + str(tds[5].text).replace(',','.') + '\n')
		f=open(mypath + 'horses.txt','a',encoding='utf8')		
		f.write(line + '\n')
		f.close()
	
		time.sleep(random.randint(1, 3))
fin.close()
fout.close()
