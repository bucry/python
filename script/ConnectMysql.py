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
 
# 引入 MySQL 模組
import MySQLdb
 
# 連接到 MySQL
db = MySQLdb.connect(host="localhost", user="db_user", passwd="db_pass", db="db_name")
cursor = db.cursor()
 
# 執行 SQL 語句
cursor.execute("SELECT * FROM db_table")
result = cursor.fetchall()
 
# 輸出結果
for record in result:
    print record[0]
