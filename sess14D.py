import mysql.connector as db


def main():
    sql1 = "update Customer set name = 'Vansh', age=13 where cid = 1"
    sql2 = "delete from Customer where cid = 2"
    sql3 = "select * from Customer"

    # Step1: Create Connection with Database
    connection = db.connect(user='root',
                            password='12345678',
                            host='127.0.0.1',
                            database='gwpds')

    # Step2: Obtain Cursor to perform SQL operations :)
    cursor = connection.cursor()

    # # Step4: Execute SQL Command
    # cursor.execute(sql1)
    # cursor.execute(sql2)
    # connection.commit()
    # print("SQL Query Executed...")
    #
    cursor.execute(sql3)
    rows = cursor.fetchall()  # fetchall-> list of tuples
    for row in rows:
        print(row)
    # print(row[0], row[1])


if __name__ == "__main__":
    main()
