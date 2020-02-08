# Copyright (c) 2020 Jan van der Meiden.                            
# Copying and distribution of this file, with or without modification, 
# are permitted in any medium without royalty provided the copyright   
# notice and this notice are preserved.  This file is offered as-is,   
# without any warranty.   
#
# This is a python script that extracts the pictures from an ldif file 
# it requires 1 parameter: the ldif file name

import sys
from ldif import LDIFParser,LDIFWriter 

class MyLDIF(LDIFParser):
   def __init__(self,input,output):
      LDIFParser.__init__(self,input)

   def handle(self,dn,entry):
      for k, v in entry.items():
        if k == 'jpegPhoto' or k =='thumbnailPhoto': 
           print(entry['userPrincipalName'][0].decode('utf-8'))
           file = open(entry['c'][0].decode('utf-8')+"."+entry['userPrincipalName'][0].decode('utf-8')+".jpg",'wb') 
           if (isinstance(v[0], (bytes, bytearray))):
               file.write(v[0]) 
           file.close()

parser = MyLDIF(open(sys.argv[1], 'rb'), sys.stdout)
parser.parse()
