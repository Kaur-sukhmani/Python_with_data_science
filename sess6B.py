# homework
# paytm
# Recharge OR Pay Mobile bill
class Recharge:
    def __init__(self, type="Prepaid", mobile_number="", operator="Jio", amount=400):
        self.type = type
        self.mobile_number = mobile_number
        self.operator = operator
        self.amount = amount


    def show(self):
        print("**************************")
        print("Type:", self.type)
        print("mobile_number:", self.mobile_number)
        print("Operator:", self.operator)
        print("Amount:", self.amount)
        print("**************************")

Customer1 = Recharge("Prepaid", "+91 9723387487", "Airtel", 500)
Customer2 = Recharge("Postpaid", "+91 9237483434", "BSNL", 200)

Customer1.show()
Customer2.show()



