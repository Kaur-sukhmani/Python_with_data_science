from sess15 import Pet
from sess14A import Customer
from sess14B import DBHelper
from sess17 import Consultation
from tabulate import tabulate


def consultation_menu():
    db = DBHelper()

    message = """
        >>Consultation Menu<<
        1. add consultation 
        2. update consultation 
        3. view all consultation
        4. view all consultation by date
        5. view customer pet consultation
        0. quit 
        """

    print(message)
    choice = int(input("Enter your choice"))
    customer = Customer()
    pet = Pet()
    consultation = Consultation()

    while True:
        if choice == 1:

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

            consultation.cid = customer.cid
            consultation.pid = pet.pid
            consultation.read_consultation_data()

            print(vars(consultation))

            sql = consultation.get_insert_sql_query()
            db.execute_sql(sql)
            print("consultation added ")

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

            sql = consultation.get_consultaion_sql_query(cid=str(customer.cid), pid=str(pet.pid))
            rows = db.execute_select_sql(sql)

            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPERATURE', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            consultation_cnid = input("Enter Consultation ID:")
            consultation_fetched = None
            for row in rows:
                if row[0] == consultation_cnid:
                    consultation_fetched = row
                    break

            if not consultation_fetched:
                print("Consultation with ID {} not found.".format(consultation_cnid))
            else:
                consultation_cnid = consultation_cnid

            consultation.problem = input("Enter problem")
            if len(consultation.problem) == 0:
                consultation.problem = consultation_fetched[3]

            consultation.heartrate = input("Enter your pets heartrate")
            if len(consultation.heartrate) == 0:
                consultation.heartrate = consultation_fetched[4]

            consultation.temperature = input("Enter your pets temperature")
            if len(consultation.temperature) == 0:
                consultation.temperature = consultation_fetched[5]

            consultation.medicines = input("Enter your pets temperature")
            if len(consultation.medicines) == 0:
                consultation.medicines = consultation_fetched[6]

            sql = consultation.get_consultaion_sql_query(customer.cid, pet.pid)
            db.execute_sql(sql)
            print("Customer Updated...")

        elif choice == 3:
            sql = consultation.get_consultaion_sql_query()
            rows = db.execute_select_sql(sql)

            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPERATURE', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 4:
            date = input("Enter date: ")
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            sql = consultation.get_consultaion_bydate_sql_query(date)
            rows = db.execute_select_sql(sql)
            # for row in rows:
            #     print(row)

            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPERATURE', 'MEDICINES', 'CREATEDON']
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

            if len(rows) == 0:
                print("please add Pet")
                break

            elif len(rows) == 1:
                pet.pid = rows[0][0]

            else:
                pet.pid = int(input("Enter pet id"))

            sql = consultation.get_consultaion_sql_query(cid=str(customer.cid), pid=str(pet.pid))
            rows = db.execute_select_sql(sql)
            # for row in rows:
            #     print(row)

            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPERATURE', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break
        else:
            print("wrong choice")
        print(message)
        choice = int(input("Enter your choice"))
