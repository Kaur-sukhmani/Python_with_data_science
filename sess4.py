#Loops
# while , for
employees = ["John", "jennie", "kim", "sia", "leo", "fionna"]
name = input("Enter Employee name to search:")
print("Length of the employees :", len(employees))
print("Employee to Search: ", name)

"""
flag = False
if name == employees[0]:
    flag = True

if name == employees[1]:
    flag = True

if name == employees[2]:
    flag = True 

  # time wastage : so to reduce we use loops 
"""

#  LINEAR SEARCH ALGO


"""
#while loop:
flag = False
idx = 0
while idx < 6: # always with while loop their is always codition 
    print ("Matching", name , "with", employees[idx])
    
    if name == employees[idx]
        flag = True 
        break # to stop the loop 
    idx += 1
"""

# for loop
flag = False
for idx in range(6):
    print("Matching", name, "with", employees[idx])

    if name == employees[idx]:
        flag = True
        break
if flag:
    print("Name found...")
else:
    print("Name not found..")

