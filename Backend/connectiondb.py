import mysql.connector


class DBconnect:
    def __init__(self):
        self.connection=mysql.connector.connect(host='Localhost', user='root',password='8A5C', database='intro_to_algo')
        self.cur = self.connection.cursor()

    #=============IUD function================================
    #==========="This function helps to execute data of insert update and delete the data"===========

    def iud(self,query=None,values=None):
        self.cur.execute(query,values)
        self.connection.commit()


    def select(self, query, values):
        self.cur.execute(query, values)
        rows = self.cur.fetchall()
        return rows

    def fetch_info(self, query,values=None):
        self.cur.execute(query,values)
        rows = self.cur.fetchall()
        return rows











