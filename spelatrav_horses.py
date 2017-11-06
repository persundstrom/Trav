# -*- coding: ISO-8859-1  -*-
import csv

import os
import sys
import codecs
import requests
koden=sys.stdin.encoding
print(sys.getdefaultencoding())
from random import randint
import random

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
mypath = 'raceday/'
import time

horses = []
drivers = []
trainers = []

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for fil in onlyfiles:
	#fil= 'raceday30360.txt''
	print(fil)
	f = open(mypath + fil,'r')
	filedata = f.readlines()
	f.close()	
	horseoutputfilename = 'horse/horse_' + fil
	driveroutputfilename = 'driver/driver_' + fil
	traineroutputfilename = 'trainer/trainer_' + fil
	fh = open(horseoutputfilename,'w')
	ft = open(traineroutputfilename,'w')
	fd = open(driveroutputfilename,'w')
	for url in filedata:
		time.sleep(random.randint(1, 4))
		print(url)
		page = requests.get(filedata[1])
		data = page.text
		soup = BeautifulSoup(data,"lxml")
		tab = soup.find('table',{'id':'myTable'})
		rows = tab.find_all('tr')
		for r in rows:
			tds = r.find_all('td')
			for td in tds:
				a = td.find('a')
				if a != None:
					if 'resultat' in str(a):
						fh.write(str(a["href"]) + '\n')
					#	horses.append(str(a["href"]))
	#					print ('hast              ' + str(a["href"]))
					if 'kuskstat' in str(a):
						fd.write(str(a["href"]) + '\n')
					#	drivers.append(str(a["href"]))
	#					print ('kuskstat              ' + str(a["href"]))
					if 'transtat' in str(a):
					#	trainers.append(str(a["href"]))
						ft.write(str(a["href"]) + '\n')
	#					print ('transtat              ' + str(a["href"]))
	fh.close()
	fd.close()
	ft.close()




