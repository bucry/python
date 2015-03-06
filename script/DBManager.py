__metaclass__ = type
import MySQLdb
import pymssql
import sys;

if not ".\\" in sys.path:
    sys.path.append(".\\")
    
if not 'TbUserEntity' in sys.modules:
    tbUserEntity = __import__('TbUserEntity')
else:
    eval('import TbUserEntity')
    tbUserEntity = eval('reload(TbUserEntity)')

class connectLocalPsotgresql():
    def initConnect(self, host, user, passwd, port, sql):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.sql = sql
        listValue = []
        conn = MySQLdb.connect(host=host, user=user, passwd=passwd, port=port)
        curs = conn.cursor()
        conn.select_db('u1wan')
        curs.execute(sql)
        row = curs.fetchone()
        while row:
            tbuser = tbUserEntity.tbUser()
            tbuser.initTbUser(row[0], row[1], row[2], row[3], row[4], row[5])
            listValue.append(tbuser)
            row = curs.fetchone()
        conn.commit()
        curs.close()
        conn.close()
        return listValue
