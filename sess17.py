# Consultation: customer, pet, problem, heartrate, temperature, medicines, createdon
# code comsultation in vetsa
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
    
    create table Consultation(
        cnid int primary key auto_increment,
        cid int,
        pid int,
        problem text,
        heartrate int,
        temperature float, 
        medicines text, 
        createdon datetime, 
        FOREIGN KEY (cid) REFERENCES Customer(cid), 
        FOREIGN KEY (pid) REFERENCES Pet(pid)
        );

"""


class Consultation:

    def __init__(self):
        self.cnid = 0
        self.cid = 0
        self.pid = 0
        self.problem = ""
        self.heartrate = 0
        self.temperature = 98.4
        self.medicines = ""
        self.createdon = ""

    def read_consultation_data(self):
        # self.cid = 0
        self.problem = input("enter Problem: ")
        self.heartrate = int(input("Enter heart rate:"))
        self.temperature = float(input("Enter Temperature"))
        self.medicines = input("Enter medicines:")

        #  get date and time
        self.createdon = str(datetime.datetime.today())
        # # eliminate milli seconds
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = "insert into Consultation values(null, {cid}, {pid} , '{problem}', {heartrate}, " \
              "{temperature}, '{medicines}', '{createdon}');".format_map(vars(self))
        return sql

    def get_consultaion_sql_query(self, cid="", pid=""):

        sql = "select * from consultation"
        if len(cid):
            sql = "select * from consultation where cid  = {}".format(cid)
        if len(pid) != 0:
            sql = "select * from consultation where pid  = {}".format(pid)
        return sql

    def get_consultaion_bydate_sql_query(self, date=""):
        sql = "select * from consultation where createdon = '{}'".format(date)
        return sql

    def get_delete_sql_query(self, pid):
        sql = "delete from consultation  where cnid = {}".format(self.cnid)
        return sql


"""
    def get_update_sql_query(self):
        sql = "update Pet set name = '{name}', age = {age}, weight = {weight}, breed = '{breed}', " \
              "gender = '{gender}' where pid = {pid}".format_map(vars(self))
        return sql 
        
"""
# agar if
