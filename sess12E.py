name = "Sukh"
age = 23
email = "sukh@gmial.com"
contact = {
 "name": "john",
 "age": 23,
 "email": "john@gmail.com"
}

print(name, age, email)
# string formatting
print("name", name, "age:",age )

print("name:{} age:{} email:{} ".format(name, age, email))
print("name:{0} age:{1} email:{2} ".format(name, age, email))
print("name:{nm} age:{ag} email:{em} ".format(nm=name, ag=age, em=email))

print("name:{name} age:{age} email:{email}".format_map(contact))