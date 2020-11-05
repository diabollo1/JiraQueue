import sys
from aifc import Error

import mysql.connector
from mysql.connector import Error

from conf import db_conf, log_conf


class DatabaseInput:
    def __init__(self):
        self.db_name = db_conf.db_name
        self.host = db_conf.host
        self.name = db_conf.name
        self.password = db_conf.password
        self.db_table_name = db_conf.db_table_name

        self.logger = log_conf.get_logger(__class__.__name__ + ".log")

        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.name,
                passwd=self.password,
                database=self.db_name
            )
            self.logger.debug("Connection to MySQL DB (" + self.host + ":" + self.db_name + ") successful")
            return connection
        except Error as e:
            self.logger.error("The error occurred: " + str(e))
            raise Error(__name__ + ":" + str(sys.exc_info()[2].tb_lineno) + "|" + str(e))

    def get_all_issue_list(self):
        try:
            sql = "SELECT * FROM "+self.db_name+"."+self.db_table_name
            myresult = self.query(sql)
            return myresult
        except Error as e:
            self.logger.error("The error occurred: " + str(e))
            raise Error(__name__ + ":" + str(sys.exc_info()[2].tb_lineno) + "|" + str(e))

    def get_issue_to_create_list(self):
        try:
            sql = "SELECT * FROM "+self.db_name+"."+self.db_table_name+" WHERE issue_date_adding is null"
            myresult = self.query(sql)
            if myresult:
                self.logger.debug("Successful get " + str(len(myresult)) + " issue from db")
                return myresult
            else:
                self.logger.info("No issue to create")
                raise ResourceWarning(__name__ + "|No issue to create")
        except Error as e:
            self.logger.error("The error occurred: " + str(e))
            raise Error(__name__ + ":" + str(sys.exc_info()[2].tb_lineno) + "|" + str(e))

    def set_data_issue(self, list_db_id, create_issue_output):
        try:
            # TODO: complete the rest fields (issue_id,issue_key,issue_url) = create_issue_output
            sql = "UPDATE " + self.db_name + "." + self.db_table_name + \
                  " SET issue_date_adding = CURRENT_TIMESTAMP WHERE id in (" + list_db_id + ")"
            rowcount = self.query(sql)
            self.connection.commit()
            self.logger.info("Successful update " + str(rowcount) + " issue in db")
            return str(rowcount) + " record(s) affected"
        except Error as e:
            self.logger.error("The error occurred: " + str(e))
            raise Error(__name__ + ":" + str(sys.exc_info()[2].tb_lineno) + "|" + str(e))

    def query(self, sql):
        mycursor = self.connection.cursor()
        self.logger.debug(sql)
        mycursor.execute(sql)
        if sql.find("SELECT") > -1:
            myresult = mycursor.fetchall()
            return myresult
        else:
            rowcount = mycursor.rowcount
            return rowcount
