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
from selenium import webdriver


import urllib

horse = []
hor = []

PHANTOMJS_PATH = 'phantomjs'


h_path = 'horse/'

h_files = [h for h in listdir(h_path) if isfile(join(h_path, h))]

h_h = open('uniqhorse.dat','r')
for i in h_h.readlines():
	horse.append(i)
h_h.close()
horse = [i.strip() for i in horse]
horse = list(sorted(set(horse) )) 

#print driver
cnt=0

for ho in horse:
	cnt=cnt+1
	hor = 'Horseresultat/' + re.sub("\D", "", ho)
	if not os.path.isfile(hor):
				
		urllib.urlretrieve(ho+'?source=S', hor)
		time.sleep(random.randint(2,7))
	print hor + "   " + str(cnt) + " av " + str(len(horse)) + " " + ho +'?source=S'
