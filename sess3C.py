# Conditional Operators

message = """
    Welcome to Zomato
    Subway offers
    WELCOME50
    get 50% of upto 100
    Valid on total value of items worth 159 or above
    ZOMPAYTM
    GET 20% DISCOUNT upto 50
"""

print(message)
amount = int(input("Enter your amount: "))
promo_code = input("Enter promocode")

# simply
"""
if amount >= 159:
    print("you can apply promocode")
else:
    print("You cannot apply promocode")
"""

#Nested if/else
"""
if amount >= 159 :
    if promo_code == "WELCOME50":
        print(" Promrocode applied successfully ")
        discount = 0.5 * amount
        if discount >= 100:
            discount = 100
        amount_to_pay = amount - discount
        print("Amount to pay :\u20b9",  amount_to_pay)
    else:
        print("Invalid promocode")
        print(f"Please pay:{amount }")
else:
    print("Invalid promocode")
"""

#Ladder if/else
if promo_code == "WELCOME50":
    if amount >= 159:
        print(" Promrocode applied successfully ")
        discount = 0.5 * amount
        if discount >= 100:
            discount = 100
        amount_to_pay = amount - discount
        print("Amount to pay :\u20b9", amount_to_pay)
    else:
        print("Invalid promocode")
        print(f"Please pay:{amount}")
elif promo_code == "ZOMPAYTM":
    if amount >= 299:
        print("Promocode applied successfully")
        discount = 0.20 * amount
        if discount >= 50:
            discount = 50
        amount_to_pay = amount -discount
        print("Amount to pay :\u20b9", amount_to_pay)
        print("You will get a cashback of \u20b9 25")
    else:
        print("Amount is less for promocode")
        print(f"Please pay \u20b9 {amount}")

else:
    print("Invalid promocode")

"""
Assignment : you need to suggest the right promocode to the user based on the amount which saves the most
"""
