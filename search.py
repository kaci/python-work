#!/usr/bin/python
# -*- coding: utf-8 -*-

# this code search in the sourche_path the list of extensions, and copy 
# these files to the dest_path, and create a file list in dest_path


import glob, os, subprocess
from shutil import copyfile

path_chdir = input('path of mounted partition: ').strip()
dest_path =  input('destination folder: ').strip()

os.chdir(path_chdir)

extensions = ['txt','TXT','pdf','PDF','xls','XLS','xlsx','XLSX', \
              'doc','DOC','docx','DOCX', 'rtf', 'RTF']

subprocess.Popen(['mkdir', dest_path], stdin = subprocess.PIPE).communicate()

with open(os.path.join(dest_path, '!file_list.info'), 'w') as file_list:
    for extension in extensions:
        for filename in glob.iglob(os.path.join('./', '**/*.') + extension, recursive=True):
            file_list.write(filename + '\n')
            copyfile(filename, os.path.join(dest_path, filename.split('/')[-1]))
