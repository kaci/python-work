#!/usr/bin/python
import magic

# check open file, is pdf?

file_type = magic.from_file("issue30_hu.pdf", mime=True)
if file_type == b'application/pdf':
    print('Yes')
