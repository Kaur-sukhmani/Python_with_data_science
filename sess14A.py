# import mysql.connector as db
import datetime

"""
       show databases;
       use gwpds;
       show tables;
       drop table Customer;
       
       
    
       create table Customer(
        cid int primary key auto_increment,
        name text,
        phone text unique key,
        email text,
        age int,
        gender text,
        address text,
        active int, #ideally by default =1
        createdon datetime
    );
       
       show tables;
       describe Customer;
       
      
"""


class Customer:

    def __init__(self):
        self.cid = 0
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.address = ""
        self.createdon = ""

    def read_customer_data(self):
        # self.cid = 0
        self.name = input("enter customer name: ")
        self.phone = input("enter customer phone: ")
        self.email = input("enter customer email: ")
        self.age = int(input("Enter customer age"))
        self.gender = input("enter customer gender(male/female):").lower()
        self.address = input("enter customer address: ")
        # get the data and time

        self.createdon = str(datetime.datetime.today())
        # # eliminate milli seconds
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    # datetime -> program, class, today ka function\

    def get_insert_sql_query(self):
        sql = "insert into Customer values(null, '{name}', '{phone}'," \
              "'{email}', '{age}', '{gender}', '{address}', '{createdon}');".format_map(vars(self))
        return sql

    def get_customers_sql_query(self, phone=""):
        if len(phone) == 0:
            sql = "select * from customer"
        else:
            sql = "select * from customer where phone  = '{}'".format(phone)
        return sql

    def get_delete_sql_query(self):
        sql = "delete from customer where cid = '{}'".format(self.cid)
        return sql

    def get_update_sql_query(self):
        sql = "update Customer set name='{name}', phone='{phone}', email='{email}', age={age}, " \
              "gender='{gender}', address='{address}' where cid = {cid}".format_map(vars(self))
        return sql

#
# def main():
#     """
#     today = str(datetime.datetime.today())
#     print(today)  # -> 2023-07-25 03:21:27.137960
#     # to remove milliseconds
#     idx = today.rindex(".")
#     today = today[: idx]
#     print(today) # ->2023-07-25 03:24:16
#     """
#
#     customer = Customer()
#     # print(vars(customer))
#     customer.read_customer_data()
#     print(vars(customer))
#
#
# if __name__ == "__main__":
#     main()
