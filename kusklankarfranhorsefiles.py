# -*- coding: utf-8 -*-

import csv
import re
import os
import sys
import codecs
import requests
import unicodedata

koden=sys.stdin.encoding
print(sys.getdefaultencoding())
reload(sys)
sys.setdefaultencoding('UTF-8')
print(sys.getdefaultencoding())
from random import randint
import random
import time

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

import urllib

h_path = 'Horseresultat/'

h_files = [h for h in listdir(h_path) if isfile(join(h_path, h))]

kusk_file = open('kusklankar', 'a')
tran_file = open('tranlankar', 'a')

for i in h_files:
	f = open(h_path + i)
	
	soup = BeautifulSoup(f.read(),"lxml")
	first = soup.find_all('table')
	for fir in first:
		trs = fir.find_all('tr')
		for t in trs:
			skriva = True
			cells = t.find_all('a', href=True)
			if len(cells) == 3:
				kusklank = cells[1]['href'] #text.replace('Ö','OO') 
				trainerlank = cells[2]['href']
				kusklank = kusklank[kusklank.find('/visa/')+6:kusklank.find('/kusk')]
				trainerlank = trainerlank[trainerlank.find('/visa/')+6:trainerlank.find('/tran')]
				print 'kusk ' + kusklank + ' trainer ' + trainerlank
			
				if kusklank.isdigit():
					kusk_file.write(kusklank + '\n')
				if trainerlank.isdigit():
					tran_file.write(trainerlank + '\n')
					
kusk_file.close()
tran_file.close()