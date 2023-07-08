# Conditional Operators
# ==, >=, <=, !=, >, <

cab_fare = 500
e_wallet = 500

print("Can I book the cab:", (e_wallet >= cab_fare))
print("Can I book the cab:", (cab_fare <= e_wallet))

email=input("Enter your email:")
password=input("Enter your password:")

print(f"Email is: {email}")
print(f"Password is: {password}")
# print("Login Status: ", email == "john@example.com")
# print("Login Status: ", password == "john@abc")

#Logical Operators : and or
print("Login status:",((email == "john@example.com") and (password == "john@abc")))

otp = 2210
user_otp = int(input("enter otp="))
print("OTP status:",otp == user_otp)

# Membership Testing
# is, is not
a = 10
b = 20
print(a is b)
print(a is not b)

"""
Assignment : Explore difference between is and ==
"""