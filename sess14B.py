import mysql.connector as db


class DBHelper:

    def __init__(self):
        """step 1 create connection with database"""
        self.connection = db.connect(user='root',
                                     password='12345678',
                                     # port = '3306
                                     host='127.0.0.1',
                                     database='gwpds')
        # step2 obtain cursor to perform SQL operations
        self.cursor = self.connection.cursor()
        print("[DBHelper] Connection created and cursor Obtained ...")

    # insert, update, delete i.e write into database
    def execute_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        # Step3: Execute SQL Command
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] SQL Statement Executed...")

    # select operation i.e. read from database
    def execute_select_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        # Step3: Execute SQL Command
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
