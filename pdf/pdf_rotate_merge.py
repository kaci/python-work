#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
This scirpt read all pdf from the file_path, merge this files and
the !merged read and rotate pages, then save !rotated file.
'''

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import sys, os, subprocess

file_ext     = 'pdf'
file_path    = '/home/bkl/scripts/pdf/pdfs'
merged_file  = os.path.join(file_path, '!merged.pdf')
rotated_file = os.path.join(file_path, '!rotated.pdf')
pdf_merger   = PdfFileMerger()
pdf_writer   = PdfFileWriter()

def list_files(path, ext):
    ''' Read all getting extension file in path and return a list. '''    
    filenames = sorted([path + '/' + x for x in os.listdir(path) if x[-3:] == ext])        
    print(filenames)
    if filenames:
        return filenames                
    else:
        print('Not found in the {} path {} extension file.'.format(path, ext))

def open_file(file_in):
    if 'linux' in sys.platform:
        subprocess.call(['xdg-open', file_in])
    else:
        os.startfile(file_in)

def merge_pdf(filenames):
    ''' From read_pdf_files() merge all file. '''    
    if filenames:
        with open(merged_file, 'wb') as pdf_out:
            for filename in filenames:
                pdf_reader = PdfFileReader(open(filename, 'rb'))
                pdf_merger.append(pdf_reader)
            pdf_merger.write(pdf_out)
    else:
        print('merge_pdf:  Not found input files.')

def rotate_pdf(file_in):
    ''' Read file_in and rotate pages. '''
    # remove last page
    rm_last = 1
    try:
        pdf_reader = PdfFileReader(open(file_in, 'rb'))
        with open(rotated_file, 'wb') as pdf_out:
            for pagenum in range(pdf_reader.numPages - rm_last):      
                page = pdf_reader.getPage(pagenum)
                if (pagenum % 2 == 0):
                    pdf_writer.addPage(page.rotateClockwise(90))
                else:
                    # 90 or 270 when not one direction
                    pdf_writer.addPage(page.rotateClockwise(90))
            pdf_writer.write(pdf_out)            
    except FileNotFoundError:
        print('rotate_pdf: Not found input file.')

if __name__ == '__main__':
    merge_pdf(list_files(file_path, file_ext))
    rotate_pdf(merged_file)
    open_file(rotated_file)
