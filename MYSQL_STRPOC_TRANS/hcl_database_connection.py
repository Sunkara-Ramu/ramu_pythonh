import mysql.connector
class MysqlDatabaseConnection:
    def connect(self,host,username,passwd,database):
        self.host=host
        self.username=username
        self.passwd=passwd
        self.database=database
        self.connection=mysql.connector.connect(host=self.host,username=self.username,password=self.passwd,database=self.dtabase)
        self.cursor=self.connection.cursor()