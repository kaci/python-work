#!/usr/bin/python
import magic

# check open file, is pdf?

a = magic.from_file("issue30_hu.pdf", mime=True)
if a == b'application/pdf':
    print('Yes')
