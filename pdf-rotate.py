#!/usr/bin/env python

# open "pdf" directory and all subdirectories
# all file rotate Clockwise 90 degrees and save same name

import sys
import os
import magic

from PyPDF2 import PdfFileWriter, PdfFileReader

for dirpaths, dirnames, filenames in os.walk("pdf"):
    for fname in filenames:
        fnamepath = dirpaths + "/" + fname
        file_type = magic.from_file(fnamepath, mime=True)
        
        if file_type == b'application/pdf':
            input = PdfFileReader(fnamepath, "rb")
            output = PdfFileWriter()

            for i in range(0,input.getNumPages()):
                output.addPage(input.getPage(i).rotateClockwise(90))

            outputStream = open(fnamepath, "wb")
            output.write(outputStream)