# Explore dictionary
# my_tuple = ()
my_tuple = tuple()
print("my tuple", my_tuple, type(my_tuple))
# wont be able to add in this
# my_list = []
my_list = list()
print(my_list, type(my_list))

my_set = {}
print(my_set, type(my_set))
# {} <class 'dict'> but thi sis em

my_set = set()
print(my_set, type(my_set))
#
# my_dict = {}
my_dict = dict()
print(my_dict, type(my_dict))

my_data = {101: "john", 201: "fionna", 301: "george", 661: "harry"}
print(my_data, type(my_data))

print("min of my data :", min(my_data))
# min of my data : 101
print("max of my data :", max(my_data))
# max of my data : 601
print("sum of my data :", sum(my_data))
# sum of my data : 1204

print(my_data[201])
print(my_data.get(201))
# dono main same o/p->fionna

my_data.pop(201)
# del my_data[201]

print(my_data)
# o/p;> {101: 'john', 301: 'george', 661: 'harry'}

my_data[775] = "Leo" #add
print(my_data)
# {101: 'john', 301: 'george', 661: 'harry', 775: 'Leo'}

my_data[775] = "kim" #update
print(my_data)
# {101: 'john', 301: 'george', 661: 'harry', 775: 'kim'}

# remove func doesnt use in this

del my_data[775]
print(my_data)

columns = ['from ', 'to']
flights = {}.fromkeys(columns, "delhi")
print(flights)
# {'from ': 'delhi', 'to': 'delhi'}

# list to dictionary

columns = ["ludhiana", "ferozpur", "moga", "jalandhar", "Bathinda"]
population = {}.fromkeys(columns, 1200)
print("population: ", population)
# population:  {'ludhiana': 1200, 'ferozpur': 3100, 'moga': 1200, 'jalandhar': 1200, 'Bathinda': 1200}

population["ferozpur"] = 3100
print("population: ", population)

# convert dict to list of tuples
items = list(population.items())
print("items")
print(items)
# o/p-> dict_items([('ludhiana', 1200), ('ferozpur', 3100), ('moga', 1200), ('jalandhar', 1200), ('Bathinda', 1200)])



