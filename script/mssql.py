import pymssql
conn=pymssql.connect(host="192.168.1.122",user="sa",password="123456",database="data")
cur=conn.cursor()

##cur.execute('insert into test(id)values(23)')
conn.commit()


cur.execute('SELECT * FROM test')
row = cur.fetchone()
while row:
    print "id=%d" % (row[0])
    row = cur.fetchone()
cur.close()
conn.close()

class dedadw():
    def dede(self):
        print ""




     
                      

class dedadw():
    def dede():
        print ""
