#!/usr/bin/env python
'''
This script parse tables of htm files
'''

import glob
from bs4 import BeautifulSoup

def trade_spider():
	for filename in glob.glob("*.htm"):
		soup = BeautifulSoup(open(filename, encoding = "ISO-8859-1"), "lxml")
		tables = soup.findAll('table', attrs={'class':'mainTable'})
		for table in tables :
			table_body = table.find('tbody')
			rows = table_body.findAll('tr', attrs={'style': 'cursor: pointer'})			
			for row in rows:
				cols = row.findAll('td')
				cols = [ele.text.strip() for ele in cols]
				f = open("adat.csv","a")
				for ele in cols:
					f.write(ele + ';')
				f.write('\n')
				f.close()				

trade_spider()
