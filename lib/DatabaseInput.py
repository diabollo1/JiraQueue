import mysql.connector
from mysql.connector import Error

from conf import db_conf


class DatabaseInput:
    def __init__(self):
        self.db_name = db_conf.db_name
        self.host = db_conf.host
        self.name = db_conf.name
        self.password = db_conf.password
        self.db_table_name = db_conf.db_table_name

        self.connection = self.create_connection()

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.name,
                passwd=self.password,
                database=self.db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            # TODO: Error handling
            print("The error occurred" + str(e))
        return connection

    def get_all_issue_list(self):
        mycursor = self.connection.cursor()

        mycursor.execute("SELECT * FROM "+self.db_name+"."+self.db_table_name)

        myresult = mycursor.fetchall()
        return myresult

    def get_issue_to_create_list(self):
        mycursor = self.connection.cursor()

        mycursor.execute("SELECT * FROM "+self.db_name+"."+self.db_table_name+" WHERE date_adding_issue is null")

        myresult = mycursor.fetchall()
        return myresult

