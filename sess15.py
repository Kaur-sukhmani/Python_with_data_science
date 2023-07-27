# primary and foreign key Relationship
# import mysql.connector as db
import datetime

# Pet: pid,name, age, weight, breed,cid, gender, createdon
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
     create table Pet(
        pid int primary key auto_increment,
        name text,
        age int,
        weight int,
        breed text,
        gender text,
        cid int,
        createdon datetime, 
        FOREIGN KEY (cid) REFERENCES Customer(cid)
    );

       show tables;
       describe Customer;


"""


class Pet:

    def __init__(self):
        self.pid = 0
        self.name = ""
        self.age = 0
        self.weight = 0
        self.gender = ""
        self.breed = ""
        self.cid = 0
        self.createdon = ""

    def read_pet_data(self):
        # self.cid = 0
        self.name = input("enter pet name: ")
        self.age = int(input("Enter pet age"))
        self.weight = input("Enter pet weight")
        self.breed = input("enter pet breed: ")
        self.gender = input("enter pet gender(male/female):").lower()
        # get the data and time

        self.createdon = str(datetime.datetime.today())
        # # eliminate milli seconds
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    # datetime -> program, class, today ka function\

    def get_insert_sql_query(self):
        sql = "insert into Pet values(null, '{name}', {age}," \
              "{weight}, '{breed}', '{gender}', {cid}, '{createdon}');".format_map(vars(self))
        return sql

    def get_pet_sql_query(self, cid=""):
        sql = "select * from Pet"
        if len(cid) != 0:
            sql = "select * from Pet where cid  = {}".format(cid)
        return sql

        # if len(cid) == 0:
        #     sql = "select * from Pet"
        # else:
        #     sql = "select * from Pet where cid  = {}".format(cid)
        # return sql


    def get_delete_sql_query(self, pid):
        sql = "delete from pet where pid = '{}'".format(pid)
        return sql

    def get_update_sql_query(self):
        sql = "update Pet set name = '{name}', age = {age}, weight = {weight}, breed = '{breed}', " \
              "gender = '{gender}' where pid = {pid}".format_map(vars(self))
        return sql


def main():
    pet = Pet()
    print(vars(pet))
    pet.read_pet_data()
    print(vars(pet))


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
if __name__ == "__main__":
    main()
