import mysql.connector


class DBconnect:
    def __init__(self):
        self.connection=mysql.connector.connect(host='Localhost', user='root',password='8A5C', database='intro_to_algo')
        self.cur = self.connection.cursor()

    def insert(self,query,values):
        self.cur.execute(query,values)
        self.connection.commit()

    def select(self,query,values):
        self.cur.execute(query,values)
        rows = self.cur.fetchall()
        return rows
