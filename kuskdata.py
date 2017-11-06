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
dri = []


d_path = 'driver/'
kusk_path = 'Kuskdata'
#fut = open()
d_files = [d for d in listdir(d_path) if isfile(join(d_path, d))]
for fil in d_files:
	h_d = open(d_path + fil,'r')
	for i in h_d.readlines():
		driver.append(i)
	h_d.close()
driver = [i.strip() for i in driver]
driver = list(sorted(set(driver)))

print len(driver)


#for dr in driver:
#	dri = re.sub("\D", "", dr)
#	urllib.urlretrieve(dr, dri)
#	print dri
#	time.sleep(random.randint(1,5))
