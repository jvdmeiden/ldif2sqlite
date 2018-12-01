#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Jan van der Meiden.
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
#
# This is a python script that transforms a specific ldif to a sqlite
# table
# Lacks elegance...

import sys
import collections
import sqlite3
from ldif3 import LDIFParser
from pprint import pprint

db = sqlite3.connect('employees.db')
c = db.cursor()
parser = LDIFParser(open(sys.argv[1], 'rb'))
date = sys.argv[2]
for dn, entry in parser.parse():
    a_displayName = None
    a_uid = None
    a_telephoneNumber = None
    a_info = None
    a_department = None
    a_company = None
    a_employeeType = None
    a_name = None
    a_manager = None
    a_country = None
    a_city = None
    a_mail = None
    a_mobile = None
    a_department = None
    a_photo = None
    for k, v in entry.items():
        if k == 'displayName': 
            a_displayName = entry['displayName'][0]
        if k == 'uid': 
            a_uid = entry['uid'][0]
        if k == 'telephoneNumber': 
            a_telephoneNumber = entry['telephoneNumber'][0]
        if k == 'info': 
            a_info = entry['info'][0]
        if k == 'department': 
            a_department = entry['department'][0]
        if k == 'company': 
            a_company = entry['company'][0]
        if k == 'employeeType': 
            a_employeeType = entry['employeeType'][0]
        if k == 'name': 
            a_name = entry['name'][0]
        if k == 'manager': 
            a_manager = entry['manager'][0].split(',')[0]
            a_manager = a_manager.split('=')[1]
        if k == 'c': 
            a_country = entry['c'][0]
        if k == 'l': 
            a_city = entry['l'][0]
        if k == 'mail': 
            a_mail = entry['mail'][0]
        if k == 'mobile': 
            a_mobile = entry['mobile'][0]
        if k == 'jpegPhoto' or k =='thumbnailPhoto': 
            a_photo = entry['userPrincipalName'][0]

    if a_photo != None:
        a_photo = a_country+"."+a_photo+"."+date+".jpg"
    if a_displayName != None:
        c.execute('''INSERT INTO employees(ldifDate,displayName,uid,telephoneNumber,info,department,company,employeeType,name,manager,country,city,mail,mobile,photo)  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (date,a_displayName,a_uid,a_telephoneNumber,a_info,a_department,a_company,a_employeeType,a_name,a_manager,a_country,a_city,a_mail,a_mobile,a_photo) )
        db.commit()

db.close()
