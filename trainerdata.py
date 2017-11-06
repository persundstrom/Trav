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

trainer = []
tra = []


t_path = 'trainer/'

t_files = [t for t in listdir(t_path) if isfile(join(t_path, t))]
for fil in t_files:
	h_t = open(t_path + fil,'r')
	for i in h_t.readlines():
		trainer.append(i)
	h_t.close()
trainer = [i.strip() for i in trainer]
trainer = list(sorted(set(trainer)))

#print driver


for tr in trainer:
	tra = re.sub("\D", "", tr)
	if not os.path.isfile(tra):
		urllib.urlretrieve(tr, tra)
		time.sleep(random.randint(1,5))
	print tra
