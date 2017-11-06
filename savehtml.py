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

from os import listdir
from os.path import isfile, join

import urllib

horse = []
hor = []

h_h = open('tra','r')
for i in h_h.readlines():
	horse.append(i)
h_h.close()
horse = [i.strip() for i in horse]
horse = list(sorted(set(horse) )) 

#print driver
cnt=0

for ho in horse:
	cnt=cnt+1
	hor = 'Trainerresultat/' + re.sub("\D", "", ho)
	if not os.path.isfile(hor):
				
		urllib.urlretrieve(ho, hor)
		time.sleep(random.randint(4,17))
	print hor + "   " + str(cnt) + " av " + str(len(horse)) + " " + ho +'?source=S'
