#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Jan van der Meiden.                            
# Copying and distribution of this file, with or without modification, 
# are permitted in any medium without royalty provided the copyright   
# notice and this notice are preserved.  This file is offered as-is,   
# without any warranty.   
#
# This is a python script that extracts the pictured from an ldif file 
# it requires 1 parameters: the ldif file name
# If you expect duplicates (like when running on ldifs from different i
# dates) dedplicate using soemething like "rdfind -makehardlinks true ."
# Works with https://pypi.org/project/ldif3/3.2.2/#files
# Do not yet really understand what I am doing here...
import sys
import collections
from ldif3 import LDIFParser

parser = LDIFParser(open(sys.argv[1], 'rb'))
for dn, entry in parser.parse():
    for k, v in entry.items():
        if k == 'jpegPhoto' or k =='thumbnailPhoto': 
            print("img/" + entry['c'][0]+"."+entry['userPrincipalName'][0]+"."+date+".jpg")
            file = open("img/" + entry['c'][0]+"."+entry['userPrincipalName'][0]+"."+date+".jpg",'wb') 
            if (isinstance(v[0], (bytes, bytearray))):
              file.write(v[0]) 
            file.close()
