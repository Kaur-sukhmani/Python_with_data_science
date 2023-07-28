from sess16A import customer_menu
from sess16B import pets_menu
from sess16C import consultation_menu
import datetime


def main_menu():
    message = """
    >>Main Menu<<
    1. manage customers 
    2. manage pet 
    3. manage consultaion 
    0. quit
    """

    print(message)
    choice = int(input("Enter your choice"))

    while True:
        if choice == 1:
            customer_menu()
        elif choice == 2:
            pets_menu()
        elif choice == 3:
            consultation_menu()
        elif choice == 0:
            break
        else:
            print("wrong choice")

        print(message)
        choice = int(input("Enter your choice"))


def main():
    date1 = datetime.datetime.today()  # to use this import datetime

    welcome = """
        =====================
        welcome to vets app 
        =====================
        """
    print(welcome)

    main_menu()

    bye_message = """
        =====================
        Thank you for using vets app 
        =====================
        """
    print(bye_message)

    date2 = datetime.datetime.today()
    print("App usage:", date2 - date1)


if __name__ == "__main__":
    main()
