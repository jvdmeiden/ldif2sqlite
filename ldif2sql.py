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
    a_capgeminiGrade = None
    a_uid = None
    a_capgeminiGlobalID = None
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
    a_capgeminiDiscipline = None
    a_capgeminiFunction = None
    a_capgeminiStartDate = None
    a_capgeminiEndDate = None
    a_capgeminiGender = None
    a_mobile = None
    a_department = None
    a_capgeminiEntity = None
    a_photo = None
    for k, v in entry.items():
        if k == 'displayName': 
            a_displayName = entry['displayName'][0]
        if k == 'capgemini-Grade': 
            a_capgeminiGrade = entry['capgemini-Grade'][0]
        if k == 'uid': 
            a_uid = entry['uid'][0]
        if k == 'capgeminiGlobalID': 
            a_capgeminiGlobalID = entry['capgeminiGlobalID'][0]
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
        if k == 'capgemini-Discipline': 
            a_capgeminiDiscipline = entry['capgemini-Discipline'][0]
        if k == 'capgemini-Function': 
            a_capgeminiFunction = entry['capgemini-Function'][0]
        if k == 'capgemini-StartDate': 
            a_capgeminiStartDate = entry['capgemini-StartDate'][0]
        if k == 'capgemini-EndDate': 
            a_capgeminiEndDate = entry['capgemini-EndDate'][0]
        if k == 'mobile': 
            a_mobile = entry['mobile'][0]
        if k == 'capgemini-Entity': 
            a_capgeminiEntity = entry['capgemini-Entity'][0]
        if k == 'capgemini-gender': 
            a_capgeminiGender = entry['capgemini-gender'][0]
        if k == 'jpegPhoto' or k =='thumbnailPhoto': 
            a_photo = entry['userPrincipalName'][0]

    if a_photo != None:
        a_photo = a_country+"."+a_photo+"."+date+".jpg"
    if a_displayName != None:
        c.execute('''INSERT INTO employees(ldifDate,displayName,capgeminiGrade,uid,capgeminiGlobalID,telephoneNumber,info,department,company,employeeType,name,manager,country,city,mail,capgeminiDiscipline,capgeminiFunction,capgeminiStartDate,capgeminiEndDate,capgeminiGender,mobile,capgeminiEntity,photo)  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (date,a_displayName,a_capgeminiGrade,a_uid,a_capgeminiGlobalID,a_telephoneNumber,a_info,a_department,a_company,a_employeeType,a_name,a_manager,a_country,a_city,a_mail,a_capgeminiDiscipline,a_capgeminiFunction,a_capgeminiStartDate,a_capgeminiEndDate,a_capgeminiGender,a_mobile,a_capgeminiEntity,a_photo) )
        db.commit()

db.close()
