## config.py
my_db={
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '1.1.1.1', # host IP
        'NAME': 'dbName',
        'USER': 'some_username',
        'PASSWORD': 'testing',
}

########################

def insertSomeFunction(Id, URL, fsp):
        if 'someString' not in URL:
                try:
                        db = MySQLdb.connect(host=config.my_db['HOST'], user=config.my_db['USER'], passwd=config.my_db['PASSWORD'],                          db=config.tagos_db['NAME'])
                        cur = db.cursor()
                        sql = "INSERT INTO videoidurl (Id, URL, fsp) VALUES ('"+Id+"','"+URL+"' ,'"+str(fsp)+"')"
                        cur.execute(sql)
                        db.commit()
                        cur.close()
                        logger.info(" url: {}  inserted".format(URL))
                except Exception,e:
                        logger.info(" url insertion failed")
                        logger.error(e)
                        cur.close()

        else:
                pass


##############################################################################################################3
###############################################################################################################
######### in django::
##settings.py
DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.mysql',
        "NAME" : "ABC",
        "HOST" : "1.1.1.1",
        "USER" : "user",
        "PASSWORD" : "password",
    },    
    'db1': {
        'ENGINE': 'django.db.backends.mysql',        
        'HOST': '1.1.1.1',
        'NAME': 'dbName',
        'USER': 'user',
        'PASSWORD': 'password',

    },
}



from django.db import connections
def insertIdAndURL(self, Id, URL):
        if 'stringSome' not in URL:
                try:
                        cur =  connections['db1'].cursor()
                        sql = "INSERT INTO dbTable (Id, URL) VALUES (%s, %s)"
                        val = (Id, URL)
                        cur.execute(sql, val)
                        cur.close()                        
                except Exception as e:                        
                        logger.error(e)
                        cur.close()

        else:
                pass


def insertIdUrlFsp(self, Id, URL, fsp):
        if 'string1' in URL or 'string2' in URL:
                try:
                        cur =  connections['db1'].cursor()
                        sql = "INSERT INTO dbTable (Id, URL, fsp) VALUES ('"+Id+"','"+URL+"' ,'"+str(fsp)+"')"
                        #val = (videoId, videoURL, fps)
                        cur.execute(sql)
                        #db.commit()
                        cur.close()                        
                except Exception as e:                        
                        logger.error(e)
                        cur.close()

        else:
                pass
