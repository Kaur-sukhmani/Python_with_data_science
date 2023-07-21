# explore set
# unique
# no duplicacy
john_followers = {"fionna", "sia", "jack", "joe", "george"}
print(john_followers, type(john_followers))
# set is unordered
# because of hashing
numbers = list(range(10, 101, 10))
print(numbers, type(numbers))

numbers = set(numbers)
print("numbers. now:", numbers, type(numbers))
numbers.add(10)
numbers.add(20)
numbers.add(101)
print("numbers after add:", numbers, type(numbers))
numbers.pop()
numbers.pop()
print("numbers after pop:", numbers, type(numbers))
# removing from the starrt

numbers.remove(50)
numbers.discard(30)
numbers.discard(50)
# remove and discard works same
print("numbers after remove:", numbers, type(numbers))

john_followers = {"fionna", "sia", "jack", "joe", "george"}
jake_followers = {"anna", "kim", "joe", "harry", "mike"}
fionna_followers = {"sia", "joe"}

print("john followers :", john_followers)
print("john followers :", jake_followers)
print("john followers :", fionna_followers)

followers = john_followers.intersection(jake_followers)
print("followers:", followers)
# ek se zyada bhi kar sakte hai use intersection
followers = john_followers.intersection(jake_followers).intersection(fionna_followers)
print("followers:", followers)

print("issubset:", fionna_followers.issubset(john_followers))
print("issuperset: ", john_followers.issuperset(fionna_followers))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

C = A - B  # b ke saree elements a main remove honge
print("C is :", C)
# C is : {1, 2, 3}

D = A & B
print("D is :", D)
# D is : {4, 5}

E = A ^ B
print("E is :", E)
# E is : {1, 2, 3, 6, 7, 8}

F = A | B
print("F is :", F)
# F is : {1, 2, 3, 4, 5, 6, 7, 8}

G = A.symmetric_difference(B)
# /explore symmetric diff ->>interview
"""
    the symmetric difference is a set operation that returns the elements that are unique to each set. 
    It is denoted by the caret (^) operator or can be achieved using the symmetric_difference() method.
    
    For two sets A and B, the symmetric difference is the set of elements that are in either A or B but not in both.
    In other words, it excludes the elements that are common to both sets.
    
    
    In simpler terms, the symmetric difference contains all the elements that are present in either A or B but not in both.
     If an element is common to both sets, it is excluded from the symmetric difference
"""


print("G is ", G)
# G is  {1, 2, 3, 6, 7, 8}

A.clear()
