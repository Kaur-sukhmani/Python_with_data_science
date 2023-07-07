# Multi Value Container

#LIST
#LIST is mutable ,indexed,duplicacy is allowed
names=["john", "jennie", "jim", "jack", "joe"]
print(names)
print(names[2])
names[2] = "fionna" # OK
print(names)

del names[1]
print(names)


names.append("george")
names.append("george") #duplicacy is allowed
print(names)