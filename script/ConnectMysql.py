import MySQLdb


db = MySQLdb.connect("localhost","root","123456","u1wan" )
cursor = db.cursor()
sql = """insert into article values (0,"woainimahah","http://www.aa.com","2012-9-8","wo","qq","skjfasklfj","2019","up")"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close



#!/usr/bin/python
 
# ���� MySQL ģ�M
import MySQLdb
 
# �B�ӵ� MySQL
db = MySQLdb.connect(host="localhost", user="db_user", passwd="db_pass", db="db_name")
cursor = db.cursor()
 
# ���� SQL �Z��
cursor.execute("SELECT * FROM db_table")
result = cursor.fetchall()
 
# ݔ���Y��
for record in result:
    print record[0]
