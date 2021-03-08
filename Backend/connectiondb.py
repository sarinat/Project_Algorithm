import mysql.connector


class DBconnect:
    def __init__(self):
        self.connection=mysql.connector.connect(host='Localhost', user='root',password='8A5C', database='intro_to_algo')
        self.cur = self.connection.cursor()

    #=============input, update and delete function================================
    #==========="This function helps to execute data of insert update and delete the data"===========

    def iud(self,query,values):
        self.cur.execute(query,values)
        return self.connection.commit()

    def select(self, query, values):
        self.cur.execute(query, values)
        rows = self.cur.fetchall()
        return rows

    def data_retrive(self,query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def show_data_p(self, qry, values):
        data = []

        self.cur.execute(qry, values)
        data = self.cur.fetchall()
        return data









