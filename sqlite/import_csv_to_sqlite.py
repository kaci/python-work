#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This script read all csv files in the given path, and create a tabele in the sqlite database.
'''

import sqlite3, csv, os, glob, codecs

source_db   = '.sqlite'
source_path = '/'
source_ext  = '*.txt'

conn = sqlite3.connect(source_db)

def open_files(source_path, source_ext):
    ''' open all files in source path, read the header, and the file content, call database funciton '''
    
    for csvfile in glob.glob(os.path.join(source_path, source_ext)):
        with open(csvfile, 'r', encoding='utf-8') as f:            
            
            # table name = source filename
            tName = os.path.basename(csvfile).split('.')[0]
            # reader = csv file content            
            reader = csv.reader(f, delimiter = ';')
            # header = column names
            header = next(reader, None)
            
            drop_create_entry(tName, reader, header)

def drop_create_entry(tName, reader, header):
    ''' drop table, create table with colummn names, and fill data '''
    
    with conn:
        cursor = conn.cursor()                
        
        # drop table
        cursor.execute('DROP TABLE IF EXISTS {0}'.format(tName))
        
        # create table
        cT = 'CREATE TABLE IF NOT EXISTS {0} (apid INTEGER PRIMARY KEY AUTOINCREMENT, {1})'.format(tName, ', '.join([h + ' TEXT' for h in header]))
        cursor.execute(cT)
        
        # data entry
        iT = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(tName, ', '.join(header), ', '.join(len(header)* ['?']))
        for data in reader:                    
            cursor.executemany(iT, [data])

if __name__ == '__main__':
    open_files(source_path, source_ext)
