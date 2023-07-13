"""
    OOPS

    1. Think of an Object
    Restaurant: name, phone, email, operating_hours, ratings, category
"""
# 2. Create a class
class Restaurant:
    pass

# 3. From the class create Real Objects in Memory :)
# Object Construction Statement
restaurant1 = Restaurant()
restaurant2 = Restaurant()
restaurant3 = restaurant1 # reference copy

# LHS restaurant1: is reference variable
# RHS: Restaurant() -> Creating an Object in HEAP in RAM

print("Restaurant1 is", restaurant1, id(restaurant1), hex(id(restaurant1)), type(restaurant1))
print("Data inside Object:", vars(restaurant1))

print("restaurant1 is:", restaurant1)
print("restaurant2 is:", restaurant2)
print("restaurant3 is:", restaurant3)


# operation on Object
# 1. Write Operation
restaurant1.name = "Table By Basant"
restaurant1.phone = "+91 9183746343"
restaurant1.email = "table@basant.com"
restaurant1.operating_hours = "1:00 to 23:00 hrs"
restaurant1.ratings = 4.5
restaurant1.category = "indian, chinese, veg"

restaurant2.name = "Mc Donald"
restaurant2.phone_number = "+91 9877916505"
restaurant2.email_address = "mcd@example.com"

print("Data Inside restaurant1's Object Now:", vars(restaurant1))
print("Data Inside restaurant2's Object Now:", vars(restaurant2))
print("Data Inside restaurant3's Object Now:", vars(restaurant3))


#Update Operation
restaurant2.phone_number = "+91 93283-83468"
restaurant3.email = "table@table.com"
restaurant3.name = "TABLE BY BASANT"

print("Data Inside restaurant1's Object Now:", vars(restaurant1))
print("Data Inside restaurant2's Object Now:", vars(restaurant2))
print("Data Inside restaurant3's Object Now:", vars(restaurant3))

#Delete opereation
del restaurant1.category
del restaurant2.email_address


# READ ALL DATA WITHIN OBJECT
print("Data Inside restaurant1's Object Now:", vars(restaurant1))
print("Data Inside restaurant2's Object Now:", vars(restaurant2))
print("Data Inside restaurant3's Object Now:", vars(restaurant3))

#READ OPERATION
print(restaurant1.name)
print(restaurant2.name)
print(restaurant3.name)

# DELETE OBJECT
# del restaurant2
del restaurant1
print("Data Inside restaurant1's Object Now:", vars(restaurant3))
