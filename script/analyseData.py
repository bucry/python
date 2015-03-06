# -*- coding:utf-8 -*-
__metaclass__ = type
import re
import os
import time
import pymssql
import logging
import logging.config
import psycopg2 as pg
import sys

if not ".\\" in sys.path:
    sys.path.append(".\\")
    
if not 'TbLogMessage' in sys.modules:
    tbLogMessage = __import__('TbLogMessage')
else:
    eval('import TbLogMessage')
    tbLogMessage = eval('reload(TbLogMessage)')

class connectLocalPsotgresql():   
    def insertIntoLocalPostgresql(self, valuesList, host, user, passwd, port):
        self.valuesList = valuesList
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        conn = pg.connect(database = 'cdncomm', host = host, user = user, password = passwd)
        curs=conn.cursor()
        for element in valuesList:
            sql = "insert into log4j (id, message) values (" + str(element.uid) + ",'" + str(element.message) + "')" 
            print sql
            try:
                curs.execute(sql)
                conn.commit()
            except Exception as err:
                print err
                conn.rollback()
            conn.close
   




##print os.getcwd()

f = open("D:\\u1wanNew.log")
listValueNew = []
line = f.readline()
while line:
    listValueOld = []
    if (len(line) > 1):
        listValueOld = line.strip().split(',')
        tbLogMessageEntity = tbLogMessage.tbLogMessage()
        tbLogMessageEntity.initTbLogMessage(listValueOld[0].strip().split(':')[1], line)
        listValueNew.append(tbLogMessageEntity)
    else:
        print line + "this null"
    line = f.readline()


if (len(listValueNew) > 0):
    dbManager = connectLocalPsotgresql()
    dbManager.insertIntoLocalPostgresql(valuesList=listValueNew, host='192.168.1.159', user='postgres', passwd='postgres', port=3306)

    for element in listValueNew:
        print element.uid
        print element.message
else:
    print "Nothing"

f.close()
