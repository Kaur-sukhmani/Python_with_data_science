import mysql.connector as db

"""
SQL
create table customer(
                    cid int primary key auto_increment,
                     name text,
                     phone text,
                     email text
                     );

                     terminal :
                        >mysql -u root -p
                        >create database gwpds;
                        >show databases;
                        >use gwpds;
                        >show tables;

                        >create table customer(
                                    cid int primary key auto_increment,
                                     name text,
                                     phone text,
                                     email text
                         );

                         >describe customer;

                    >insert into Customer values(null,'sukhmani', '+9183794355', 'john@example.com');
                    >select * from Customer;
"""


class Customer:

    def __init__(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")


def main():
    customer = Customer()
    print(vars(customer))

    # DataBase Connectivity

    # Step1: Create Connection with Database
    connection = db.connect(user='root',
                            password='12345678',
                            host='127.0.0.1',
                            database='gwpds')

    # Step2: Obtain Cursor to perform SQL operations :)
    cursor = connection.cursor()

    # Step3: Create SQL Statement
    sql = "insert into Customer values" \
          "(null, '{name}', '{p`hone}', '{email}');".format_map(vars(customer))

    # Step4: Execute SQL Command
    cursor.execute(sql)
    connection.commit()

    print("Customer Inserted...")


if __name__ == "__main__":
    main()

# name wagera should be singlw comma
# auto_increment->automatic increment by 1
# """
#     SQL Commands:
#
#     > create database gwpds;
#     > show databases;
#     > use gwpds;
#     > show tables;
#
#     > create table Customer(
#         cid int primary key auto_increment,
#         name text,
#         phone text,
#         email text
#       );
#
#     describe Customer;
#
#     insert into Customer values(null, 'John', '+91 99999 11111', 'john@example.com');
#     select * from Customer;
# """


