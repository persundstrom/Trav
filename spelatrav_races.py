from bs4 import BeautifulSoup
import os,urllib, sys
import time
import requests
import random

raceday = 26778	
while raceday > 20000:
	url = "https://spelatrav.se/raceday/" + str(raceday)
	r=requests.get(url)
	data =r.text
	soup = BeautifulSoup(data,"lxml")
	if 'Whoops' not in soup.text:
		if 'Denna sida finns inte!' not in soup.text: 
			ul = soup.find('ul',{'class':'pagination'})
			links = [a["href"] for a in ul.select("a[href]")]
			print (links)
			print('\n')
			outfil= 'raceday/raceday' + str(raceday) + '.txt'
			f = open(outfil, 'w')
			for i in links:
				f.write(i + '\n')
			f.close()	
	time.sleep(random.randint(1, 4)) 
	raceday = raceday - 1
	print (raceday)
	print('\n')
	