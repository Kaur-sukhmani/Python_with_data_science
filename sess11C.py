# for each or enhanced for loop
data = list(range(10, 101, 10))
print(data)
for idx in range(len(data)):
    print(idx, data[idx])

# element cna be anything of your choice
for element in data:
    print(element)

# work for -> list , tuple, set
data = set(data)
for element in data:
    print(element)

student = {
    "rollno": 101,
    "name": "fionna",
    "age": 21
}
print("dictionary data:")
items = student.items()
for item in items:
    # print(item)
    print(item[0], item[1])  # 0 is key and 1 is value

print("dictionary keys only:")
keys = student.keys()
for key in keys:
    print(key)

print("dictionary keys and values :")
for key in student:
    print(key)
    print(student[key])


