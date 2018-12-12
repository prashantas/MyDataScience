# https://github.com/nestordeharo/mysql-python-class/blob/master/mysql_python.py
import MySQLdb
from config import *
from collections import OrderedDict
import datetime


class MysqlPython(object):
    """
        #https://github.com/nestordeharo/mysql-python-class/blob/master/mysql_python.py
        Python Class for connecting  with MySQL server and accelerate development project using MySQL
        Extremely easy to learn and use, friendly construction.
    """

    __instance   = None
    __host       = None
    __user       = None
    __password   = None
    __database   = None
    __session    = None
    __connection = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance or not cls.__database:
             cls.__instance = super(MysqlPython, cls).__new__(cls,*args,**kwargs)
        return cls.__instance
    ## End def __new__

    def __init__(self, host=DB_IP, user=DB_user, password=DB_password, database=DB_name):
        self.__host     = host
        self.__user     = user
        self.__password = password
        self.__database = database
        print("#####__init__ {}, {}, {}, {}".format(self.__host, self.__user, self.__password, self.__database))
    ## End def __init__

    def __open(self):
        try:
            cnx = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database)
            self.__connection = cnx
            self.__session    = cnx.cursor()
        except MySQLdb.Error as e:
            print "error in connecting...Error %d: %s" % (e.args[0],e.args[1])
    ## End def __open

    def __close(self):
        self.__session.close()
        self.__connection.close()
    ## End def __close
    def select(self, table, where=None, *args, **kwargs):
        result = None
        query = 'SELECT '
        keys = args
        values = tuple(kwargs.values())
        l = len(keys) - 1

        for i, key in enumerate(keys):
            query += "`"+key+"`"
            if i < l:
                query += ","
        ## End for keys

        query += 'FROM %s' % table

        if where:
            query += " WHERE %s" % where
        ## End if where

        self.__open()
        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]
        self.__close()

        return result
    ## End def select
    def update(self, table="tblCrawler", where=None, *args, **kwargs):
        query  = "UPDATE %s SET " % table
        keys   = kwargs.keys()
        values = tuple(kwargs.values()) + tuple(args)
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += "`"+key+"` = %s"
            if i < l:
                query += ","
            ## End if i less than 1
        ## End for keys
        query += " WHERE %s" % where

        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()

        # Obtain rows affected
        update_rows = self.__session.rowcount
        self.__close()

        return update_rows
    ## End function update
    def insert(self, table='tblCrawler', *args, **kwargs):
        values = None
        query = "INSERT INTO %s " % table
        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query += "(" + ",".join(["`%s`"] * len(keys)) %  tuple (keys) + ") VALUES (" + ",".join(["%s"]*len(values)) + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"]*len(values)) + ")"

        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()
        self.__close()
        return self.__session.lastrowid
    ## End def insert
    def delete(self, table="tblCrawler", where=None, *args):
        query = "DELETE FROM %s" % table
        if where:
            query += ' WHERE %s' % where

        values = tuple(args)

        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()

        # Obtain rows affected
        delete_rows = self.__session.rowcount
        self.__close()

        return delete_rows
    ## End def delete
    def select_advanced(self, sql, *args):
        od = OrderedDict(args)
        query  = sql
        values = tuple(od.values())
        self.__open()
        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]

        self.__close()
        return result
    ## End def select_advanced
## End class
def getFeedid(vendor=None):
    date_ = datetime.datetime.now().strftime ("%d%m%Y")
    if vendor is not None:
        feedid = date_ + '_' + vendor
    else:
        feedid = date_
    return feedid

def readQuery():
        conditional_query = 'feedid = %s '
        connect_mysql = MysqlPython()
        feedid = getFeedid("myntra")
        result = connect_mysql.select('tblCrawler', conditional_query, 'failed_item', 'total_item', feedid=feedid)
        print("update result: {}".format(result))

def updateQuery():
        global feedid
        #feedid= '11122018_myntra'
        '''
        conditional_query = 'car_make = %s'
        result = connect_mysql.update('car_table', conditional_query, 'nissan', car_model='escort', car_year='2005')
        '''
        conditional_query = 'feedid = %s '
        connect_mysql = MysqlPython()
        #feedid = getFeedid("myntra")
        result = connect_mysql.update('tblCrawler', conditional_query,feedid , failed_item=5)
        print("update result: {}".format(result))
def readItem(item):
        global feedid
        #feedid= '11122018_myntra'
        conditional_query = 'feedid = %s '
        connect_mysql = MysqlPython()
        result = connect_mysql.select('tblCrawler', conditional_query, item, feedid=feedid)
        print("result: {}".format(result[0]))
        return result[0]

def updateItem(item):
        global feedid
        #feedid= '11122018_myntra'
        val_item = readItem(item)
        val_item = val_item + 1

        conditional_query = 'feedid = %s '
        connect_mysql = MysqlPython()
        if item == 'failed_item':
                result = connect_mysql.update('tblCrawler', conditional_query,feedid , failed_item=val_item)
        elif item == 'duplicate_item':
                result = connect_mysql.update('tblCrawler', conditional_query,feedid , duplicate_item=val_item)
        elif item == 'incomplete_item':
                result = connect_mysql.update('tblCrawler', conditional_query,feedid , incomplete_item=val_item)
        elif item == 'successful_item':
                result = connect_mysql.update('tblCrawler', conditional_query,feedid , successful_item=val_item)
        elif item == 'total_item':
                result = connect_mysql.update('tblCrawler', conditional_query,feedid , total_item=val_item)
        else:
                pass
        print("update result: {}".format(result))
def insertFeedId(feedid):
        #feedid = getFeedid("myntra")
        connect_mysql = MysqlPython()
        result = connect_mysql.insert(feedid=feedid)
#CREATE TABLE tblCrawler(Id INT NOT NULL AUTO_INCREMENT,feedid VARCHAR(40) DEFAULT NULL,total_item INT DEFAULT NULL,duplicate_item INT DEFAULT NULL,incomplete_item INT DEFAULT NULL,failed_item INT DEFAULT NULL,successful_item INT DEFAULT NULL,PRIMARY KEY (Id));
if __name__ == '__main__':
        #insertQuery()
        #updateQuery()
        #readItem('failed_item')
        updateItem('failed_item')
