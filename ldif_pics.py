# Copyright (c) 2020 Jan van der Meiden.                            
# Copying and distribution of this file, with or without modification, 
# are permitted in any medium without royalty provided the copyright   
# notice and this notice are preserved.  This file is offered as-is,   
# without any warranty.   
#
# This is a python script that extracts the pictured from an ldif file 
# it requires 2 parameters: the ldif file name and the date from the ldif file
# (too lazy to extract this from something else)
# It writes the images to a folder img

import chardet
import sys
from ldif import LDIFParser,LDIFWriter

class MyLDIF(LDIFParser):
   def __init__(self,input,output):
      LDIFParser.__init__(self,input)

   def handle(self,dn,entry):
      for k, v in entry.items():
        if k == 'jpegPhoto' or k =='thumbnailPhoto': 
           id=entry['mail'][0].decode('utf-8')
           if id:
              print(id)
           else: 
              id=entry['userPrincipalName'][0].decode('utf-8')
              print(id) 
           file = open(entry['c'][0].decode('utf-8')+"."+id+".jpg", mode='wb') 
           if (isinstance(v[0], (bytes, bytearray))):
               file.write(v[0]) 
           file.close()

with open(sys.argv[1], 'rb') as rawdata:
        result = chardet.detect(rawdata.read())
parser = MyLDIF(open(sys.argv[1], mode='r',  encoding=result['encoding']), sys.stdout)
parser.parse()
