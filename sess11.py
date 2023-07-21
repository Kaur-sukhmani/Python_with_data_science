# Multi value containers:
# list, set, dict

# EXPLORE LIST IN PYTHON

numbers = list(range(10, 101, 10))
print(numbers)
print("type of numbers :", type(numbers))

numbers.append(30)  # add in the end of the list
numbers.append(77)
numbers.append(50)
print("2. numbers", numbers)

print("Sum:", sum(numbers))
print("max:", max(numbers))
print("length:", len(numbers))
print("min:", min(numbers))

reverse_numbers = reversed(numbers)
print("reverse number:", reverse_numbers)
# reverse number: <list_reverseiterator object at 0x1043cfc40>

reverse_numbers = list(reversed(numbers))
print("reverse number:", reverse_numbers)

# can find the index of a number

print("Index of a number(50):", numbers.index(50))
print("count of 30 in numbers :", numbers.count(30))

data = [70, 30, 50, 90, 20]
print("data:", data)
data.sort()  # sorting is of combination of merge sort and insertion sort
print("data in sorted arrangement:", data)

names = ["john", "anna", "sia", "kim"]
names.sort()
print("names in sorted order:", names)
print("minimum of names:", min(names))
print("maximum of names:", max(names))
# print("sum  of names", sum(names))  # error

names.remove("sia")
# or del names[2]
data.remove(30)

print(names)
print(data)

data = [10, 20, 30, 40, 50]
# data.pop()
# print(data)  # [10, 20, 30, 40]
# can use same list as stack
# data.pop(0)
# to use as a queue use pop main value
# print(data)

# data.clear()
# print(data)
# eg clear the chat conversation on watsapp

data.insert(2, 77)
# 2 is index and 77 is value
print(data)

# to insert at the last
data.insert(-1, 99)
print(data)
# [10, 20, 77, 30, 40, 99, 50]

data.insert(len(data), 80)
print(data)
# [10, 20, 77, 30, 40, 99, 50, 80]

