__metaclass__ = type
import MySQLdb
import pymssql
import logging
import logging.config
import psycopg2 as pg
import sys

if not ".\\" in sys.path:
    sys.path.append(".\\")
    
if not 'TbUserEntity' in sys.modules:
    tbUserEntity = __import__('TbUserEntity')
else:
    eval('import TbUserEntity')
    tbUserEntity = eval('reload(TbUserEntity)')



logging.config.fileConfig("logging.conf")

#create logger
logger = logging.getLogger("example")

#"application" code
#logger.debug("debug message")
#logger.info("info message")
#logger.warn("warn message")
#logger.error("error message")
#logger.critical("critical message")

#logHello = logging.getLogger("hello")
#logHello.info("Hello world!")
    

##
class connectLocalPsotgresql():
    def initConnect(self, host, user, passwd, port, sql):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.sql = sql
        listValue = []
        ###conn = MySQLdb.connect(host=host, user=user, passwd=passwd, port=port)
        conn = pg.connect(dbname = 'u1wan', host = host, user = user, passwd = passwd)
        logger.info("conn mysql start----")
        curs = conn.cursor()
        conn.select_db('u1wan')
        curs.execute(sql)
        row = curs.fetchone()
        while row:
            tbuser = tbUserEntity.tbUser()
            tbuser.initTbUser(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            listValue.append(tbuser)
            row = curs.fetchone()
        conn.commit()
        curs.close()
        conn.close()
        return listValue
    def insertIntoLocalPostgresql(self, valuesList, host, user, passwd, port):
        ##conn=MySQLdb.connect(host = host, user = user, passwd = passwd ,port = port)
        conn = pg.connect(dbname = 'u1wan', host = host, user = user, passwd = passwd)
        logger.info("conn mysql start----")
        curs=conn.cursor()
        for element in valuesList:
            sql = "insert into u1wan.tbUser (uid, did, passwd, is_sync, is_update_pass, nickname, username) values (" + str(element.uid) + "," + str(element.did) + ",'" + element.passwd + "','" + element.isSys + "','" + element.isUpdatePass + "','" + element.nickname +"'," + element.username + "')" 
            print sql
            try:
                curs.execute(sql)
                conn.commit()
            except Exception as err:
                print err
                conn.rollback()
            conn.close
    def updateLocalPostgresql(self, valuesList, host, user, passwd, port):
        ##conn=MySQLdb.connect(host = host, user = user, passwd = passwd ,port = port)
        conn = pg.connect(database = 'u1wan', host = host, user = user, password = passwd)
        logger.info("conn mysql start----")
        curs=conn.cursor()
        for element in valuesList:
            sql = "update tbUser set is_sync = 'Y', is_update_pass='N', passwd='" + element.passwd + "', nickname = '" + element.nickname + "' where uid = " + str(element.uid)
            logger.info("update mysql start----")
            print sql
            try:
                curs.execute(sql)
                conn.commit()
                logger.info("update mysql success----")
            except Exception as err:
                print err
                logger.info("update mysql failed----")
                conn.rollback()
            conn.close


class connectRemoteMSSQLServer():   
    def initConnect(self, host, user, passwd, sql):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.sql = sql
        self.types = types
                
    def insertIntoMSSQL(self, host, user, passwd, port, sql):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.sql = sql
        connMSSQL=pymssql.connect(host=host, user=user, password=passwd, database="u1wan")
        logger.info("conn MSSQL start----")
        cur=connMSSQL.cursor()
        cur.execute(sql)
        connMSSQL.commit()
        
    def queryMSSQL(self, host, user, passwd, sql):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.sql = sql
        listValue = []
        connMSSQL=pymssql.connect(host=host, user=user, password=passwd, database="u1wan")
        logger.info("conn MSSQL start----")
        cur=connMSSQL.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        while row:
            tbuser = tbUserEntity.tbUser()
            tbuser.initTbUser(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            listValue.append(tbuser)
            row = cur.fetchone()
        cur.close()
        connMSSQL.close()
        return listValue
                      
class connectMain():
    def initMain(self):
        try:
            dbMSSQLManager = connectRemoteMSSQLServer()
            ##dbMSSQLManager.initConnect(host = '192.168.1.122',user = 'sa', passwd = '123456', sql = 'select * from test', types = 'Q')
            ##queryMSSQL
            
            values = dbMSSQLManager.queryMSSQL(host = '192.168.1.122',user = 'sa', passwd = '123456', sql = "select * from tbUser where is_update_pass = 'Y'")
            
            #dbManager = connectLocalPsotgresql()
            #values = dbManager.initConnect(host='192.168.1.122', user='root', passwd='123456', port=3306, sql = "select * from  tbUser where is_update_pass = 'Y'")
            ##dbManager.insertIntoLocalPostgresql(valuesList = values, host='192.168.1.122', user='root', passwd='123456', port=3306)
            ##dbManager.updateLocalPostgresql(valuesList = values, host='192.168.1.122', user='root', passwd='123456', port=3306)

            if (len(values) > 0) :
                print "found new data"
                dbManager = connectLocalPsotgresql()
                ###dbManager.updateLocalPostgresql(valuesList = values, host='192.168.1.122', user='root', passwd='123456', port=3306)
                dbManager.updateLocalPostgresql(valuesList = values, host='192.168.1.159', user='postgres', passwd='postgres', port=3306)
            else:
                print "no new data"
            #for element in values:
                #print element.uid
        except MySQLdb.Error,e:
             logger.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
             print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == '__main__':
    connectMain().initMain()
