# html tables pharse csv

import glob, codecs, csv
from bs4 import BeautifulSoup

# glob - unix like pathname
# codecs - character decoding, encoding
# csv - csv file reading and writing

with codecs.open('/home/lacika/melo/nav_20151014/vatera.csv', 'w', 'iso-8859-2') as csvfile:
	for filename in glob.glob('/home/lacika/melo/nav_20151014/html/*.htm'):
		data_file = codecs.open(filename, 'r', 'iso-8859-2').read()
		soup = BeautifulSoup(data_file.replace('&', '"&"'), 'html.parser')
		for row in soup.find_all('tr'):
			writer = csv.writer(csvfile, delimiter=';')
			writer.writerow(row.stripped_strings)

# input file: *.html in the running directory
# output file:  feldolg.csv
# in the input file replace & character to "&"
# search <tr> and </tr> and write the rows to one row
