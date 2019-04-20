# Copyright (c) 2018 Jan van der Meiden.                            
# Copying and distribution of this file, with or without modification, 
# are permitted in any medium without royalty provided the copyright   
# notice and this notice are preserved.  This file is offered as-is,   
# without any warranty.   
#
# This is a python script that extracts the pictured from an ldif file 
# it requires 2 parameters: the ldif file name and the date from the ldif file
# (too lazy to extract this from something else)
# It writes the images to a folder img
#
# Requires ldif3: 
# > pip install ldif3
import sys
import collections
from ldif3 import LDIFParser

parser = LDIFParser(open(sys.argv[1], 'rb'))
date = sys.argv[2]
for dn, entry in parser.parse():
    for k, v in entry.items():
        if k == 'jpegPhoto' or k =='thumbnailPhoto':
            print(entry['userPrincipalName'][0])
            print("img/" + entry['c'][0]+"."+entry['userPrincipalName'][0]+"."+date+".jpg")
            file = open("img/" + entry['c'][0]+"."+entry['userPrincipalName'][0]+"."+date+".jpg",'wb')
            if (isinstance(v[0], (bytes, bytearray))):
              file.write(v[0])
            file.close()

