#!/usr/bin/env python 
import psycopg2
conn= psycopg2.connect("user=adadmin dbname=admanager") 
cur = conn.cursor() 
cur.execute('SELECT * FROM loginuser') 
rows = cur.fetchall() 
for i in rows: 
    print i 
cur.close() 
conn.commit() 
conn.close() 
