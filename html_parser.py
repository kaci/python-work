#!/usr/bin/env python
'''
This script find the users in the htm files
'''

import requests
import time
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://www...' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, 'lxml')
		divs = soup.findAll('div', {'class': 'rating-name'})
		f = open("felhasznalok.txt","a")
		for div in divs:
			f.write(div.find('a')['href']+"\n")
		f.close()
		page += 1		
		time.sleep(3)

trade_spider(1)
