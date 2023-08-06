from sess15 import Pet
from sess14A import Customer
from sess14B import DBHelper
from tabulate import tabulate


def pets_menu():
    db = DBHelper()

    message = """
        >>Pet Menu<<
        1. add pet
        2. update pet
        3. delete pet 
        4. view all pets
        5. view customer pets
        0. quit 
        """

    print(message)
    choice = int(input("Enter your choice"))
    customer = Customer()
    pet = Pet()
    while True:
        if choice == 1:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            # customer_fetched = rows[0]
            # customer.cid = customer_fetched[0]
            #
            # pet.cid = customer.cid

            pet.cid = rows[0][0]

            pet.read_pet_data()
            print(vars(pet))

            sql = pet.get_insert_sql_query()
            db.execute_sql(sql)
            print("pet added ")

        elif choice == 2:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            if len(rows) == 0:
                print("please add Pet")
                break

            elif len(rows) == 1:
                pet.pid = rows[0][0]

            else:
                pet.pid = int(input("Enter pet id"))

            pet_fetched = None
            for row in rows:
                if row[0] == pet.pid:
                    pet_fetched = row
                    break

            if not pet_fetched:
                print("Pet with ID {} not found.".format(pet.pid))
            else:
                pet.pid = pet.pid

            pet.name = input("Enter pet Name: ")
            if len(pet.name) == 0:
                pet.name = pet_fetched[1]

            pet.age = input("Enter Pet Age: ")
            if len(pet.age) == 0:
                pet.age = pet_fetched[2]
            else:
                pet.age = int(pet.age)

            pet.weight = input("Enter pet weight: ")
            if len(pet.weight) == 0:
                pet.weight = pet_fetched[3]
            else:
                pet.weight = int(pet.weight)

            pet.breed = input("Enter pet breed: ")
            if len(pet.breed) == 0:
                pet.breed = pet_fetched[4]

            pet.gender = input("Enter pet Gender: ")
            if len(pet.gender) == 0:
                pet.gender = pet_fetched[5]

            sql = pet.get_update_sql_query()
            db.execute_sql(sql)
            print("Pet Updated...")


        elif choice == 3:

            phone = input("Enter Customer phone : ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            pet.pid = int(input("enter pet id:"))
            delete_choice = input("Are Your Sure to Delete ? (yes/no): ")

            if delete_choice == "yes":
                sql = pet.get_delete_sql_query(pet.pid)
                db.execute_sql(sql)
                print("Pet Deleted...")

        elif choice == 4:
            sql = pet.get_pet_sql_query()
            rows = db.execute_select_sql(sql)
            # for row in rows:
            #     print(row)

            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 5:

            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break
        else:
            print("wrong choice")
        print(message)
        choice = int(input("Enter your choice"))
