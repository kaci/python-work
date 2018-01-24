#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, shutil, csv

srcroot = input('source folder: ').strip()
dstroot = input('destination folder: ').strip()

extensions = ['doc', 'docx', 'xls', 'xlsx', 'pdf', 'odf', 'rtf', 'txt', 'csv']

def walk_and_copy(srcroot, dstroot, extensions):
    ''' walk on srcroot, and create same dirs in dstroot, and copy files in extensions '''
    
    # walk on srcroot
    for path, dirs, files in os.walk(srcroot):
        
        # new_path in dstroot
        new_path = path.replace(srcroot, dstroot)
        
        # create dir if no exists
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        
        # create csv file
        with open(dstroot + '/!file_list.csv', 'a', newline='', encoding = 'utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';')
            
            # iter all filenames in path, and copy this to the dstroot, when in extensions
            for filename in files:        
                if filename.lower().split('.')[1] in extensions:
                    shutil.copy2(path + '/' + filename, new_path)                
                    try:
                        spamwriter.writerow([path.replace(srcroot, ''), filename])
                    except UnicodeEncodeError:
                        print(path, filename)

if __name__ == '__main__':
    walk_and_copy(srcroot, dstroot, extensions)
