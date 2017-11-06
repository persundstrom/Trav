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

driver = []
cnt=0
year = []
starter = []
a1 = []
a2 = []
a3 = []
peng = []
cells = []

bana = []
lopp = []
datum = []

resultat = []

spar = []
distans = []
tid = []
start = []
hast = []
trainer = []
lopptyp = []
odds = []
skofram = []
skobak = []
skor = []
kusk = []
trainer = []

h_path = 'Horseresultat/'
h_file = '557301'
loppcnt=0

utstr = []
utstring = ''
utstring2 = ''
utstring3 = ''

h_files = [h for h in listdir(h_path) if isfile(join(h_path, h))]
#print h_files

header = 'horsename' + '\t' + 'sex' + '\t' + 'fodd' + '\t' + 'ras' + '\t' + 'avelsindex1' + '\t' + 'avelsindex2' + '\t' + 'inavel'
header = header + '\t' + 'bana' + '\t' + 'datum' + '\t' + 'lopp' + '\t' +'spar' + '\t' + 'distans' + '\t' + 'distansbonus' + '\t' + 'lopptypM' + '\t' + 'lopptypB' + '\t' + 'resultat' + '\t' + 'odds' + '\t'
header = header + 'tid' + '\t' + 'tidG' + '\t' + 'tidA' + '\t' + 'skofram' + '\t' + 'skobak' + '\t' + 'kusk' + '\t' + 'trainer'
out_file = open('out_file4', 'a')
out_file.write(header + '\n')

for i in h_files:
	utstring = ''
	utstring2 = ''
	utstring3 = ''
	print i
#	f = open(h_path + h_file)
	f = open(h_path + i)
	
	soup = BeautifulSoup(f.read(),"lxml")
#	content = soup.find("div",{"id":"content"})
#	tab = content.find('div',{'class':'tab-panel'})
	first = soup.find_all('table')
	h1 = soup.find_all('h1')
	skriva = True
	if len(h1)>0:
		utstring3 = h1[1].span.text.replace('Ö','OO')
		namn = True
	else:
		namn = False
		skriva = False
	inavel = False
	Bana = False
	for fir in first:
		
	#	print "innan inavel   " + str(skriva)
		if 'Inavelsko' in str(fir) and skriva and namn:
			trs = fir.find_all('tr')
			
			cells = trs[1].find_all('td')
	#		print cells[4].text
			if ' ' in cells[4].text:
				avind = cells[4].text[:cells[4].text.index(' ')]
				avind2 = cells[4].text[cells[4].text.index(' ')+1:]
				if cells[3].text == 'kallblodig travare' or cells[3].text == 'varmblodig travare' or cells[3].text == 'valrmblodig travare':
					utstring = cells[1].text + '\t' + cells[2].text[:4] + '\t' + cells[3].text + '\t' + avind + '\t' + avind2.replace(',','.') + '\t' + cells[5].text.replace(',','.')
				else:
					skriva = False
				inavel = True
			else:
				skriva = False
			
	#	print "efter inavel   " + str(skriva) + str(namn)		
		if 'Bana' in str(fir) and skriva and namn:
			loppcnt = loppcnt + 1
	#		print "bana table " + str(skriva)
			utstr = []
			trs = fir.find_all('tr')
			for t in trs:
				skriva = True
				cells = t.find_all('td')
			#	print "find all td " + str(skriva)
				if len(cells)>0  and skriva:
					if not cells[0].text:
						skriva = False
	#					print "bana false" + str(cells[0].text)
					else:
						utstring2 = cells[0].text.replace('Ö','OO') + '\t'
	#					print "bana"
										
					if skriva == True and '-' in str(cells[1].text):						 
						utstring2 = utstring2 + str(cells[1].text)[:6] + '\t' + str(cells[1].text)[7:] + '\t'
			#			print cells[1].text
					else:
						skriva = False
				#		print 'datum false ' + cells[1].text
										
					if skriva == True:
						sp = cells[3].text
						slashpos = sp.find('/')
						if sp[-1:].isdigit():
							utstring2 = utstring2 + sp[:slashpos] + '\t' + sp[slashpos+1:slashpos+5] + '\t' + 'unknown'
						else:
							utstring2 = utstring2 + sp[:slashpos] + '\t' + sp[slashpos+1:slashpos+5] + '\t' + sp[slashpos+5:]
				#		print "spar distans"
						
				#	print cells[4].text
				#	print skriva
					
					if skriva == True:
						if 'm' in cells[3].text:
							utstring2 = utstring2 + '\t' + '1'
						else:
							utstring2 = utstring2 + '\t' + '0'
						if 'b' in cells[3].text:
							utstring2 = utstring2 + '\t' + '1'
						else:
							utstring2 = utstring2 + '\t' + '0'
					
					
					if skriva == True:
						if cells[4].text.isdigit() and cells[4].text != '0':
							utstring2 = utstring2 + '\t' + cells[4].text
				#			print "resultat"
						else:
							skriva = False
				#			print "reulse false  " + str(cells[4].text)
							 
					if skriva == True:
						if not cells[6].text.isdigit():
							skriva = False
	#						print "odds false"
						else:
							utstring2 = utstring2 + '\t' + cells[6].text
	#						print "odds"
						
					if skriva == True:			
						if 'it' in cells[5].text or 'ug' in cells[5].text or 'nd' in cells[5].text or 'dist' in cells[5].text or ',' not in cells[5].text:
							skriva = False
				#			print "tid false"
				#			print cells[5].text
						else:
							kommapos = cells[5].text.find(',')
							utstring2 = utstring2 + '\t' + cells[5].text[:kommapos+2].replace(',','.')
							if 'g' in cells[5].text:
								utstring2 = utstring2 + '\t' + '1' 
							else:
								utstring2 = utstring2 + '\t' + '0'
							if 'a' in cells[5].text:
								utstring2 = utstring2 + '\t' + '1' 
							else:
								utstring2 = utstring2 + '\t' + '0'
				#			print "tid"
							
					if skriva == True:
						if cells[7].find('img') and skriva == True:
							skor = cells[7].find_all('img')
							if 'EjSko' in str(skor[0]):
								utstring2 = utstring2 + '\t' + '0'
							else:
								utstring2 = utstring2 + '\t' + '1'
							if 'EjSko' in str(skor[1]):
								utstring2 = utstring2 + '\t' + '0'
							else:
								utstring2 = utstring2 + '\t' + '1'
				#			print "skor"
						else:
							skriva = False
			#				print "skor false"
	#				print 'slrova  ' + str(skriva)	
					if skriva == True:
						utstring2 = utstring2 + '\t' + cells[8].find('span').text.replace('Ö','OO') + '\t' + cells[9].find('span').text.replace('Ö','OO')
				
					if skriva == True:
	#					print "apppendnde   " + str(skriva)
						utstr.append(utstring2)
						Bana = True
		#			print "efter baan " + str(skriva)		
	#print "len utstr    " + str(len(utstr)) + "   " + str(skriva) + "inavel  " + str(inavel) + "  Bana  " + str(Bana) #+ "utstr3 " + utstring3 + "  utstring " + utstring
	
	#if skriva == True:
	if Bana == True and inavel == True and namn:
		for r in utstr:	
			ut =  utstring3 + '\t' + utstring + '\t' + r
			cnt = cnt + 1			
			out_file.write(ut.encode('UTF-8', 'ignore').decode('UTF-8').replace('ä','a').replace('Ä','A').replace('å','a').replace('Å','A').replace('ö','o').replace('O','O') + '\n') 
		utstring = ''
		utstring2 = ''
		utstring3 = ''	
		print "loppcnt     " + str(loppcnt)
		print "Cnt: " + str(cnt)

