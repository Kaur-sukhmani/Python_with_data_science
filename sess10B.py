"""
    Multi value container
    SEQUENCE:
        tuple
        list
        set -> 1D
        string

    properites :
    1. Indexing                -  list , tuple
    2. Negative indexing       -
    3. Slicing                 -
    4. Concatenation           -
    5. Multiplicity            -
    6. Membership Testing      -

dictionary

"""
# 1D list
#         0     1   2
#         -3   -2  -1
# my_data = [10, 20, 30]
my_data = (10, 20, 30)
# my_data = {10, 20, 30}
# 2D list
# numbers = [
#     [10, 20, 30],
#     [40, 50, 60, 70, 80],
#     [90, 99]
# ]
numbers = (
    (10, 20, 30),
    (40, 50, 60, 70, 80),
    (90, 99)
)
"""
error in 2D in set
numbers = {
    {10, 20, 30},
    {40, 50, 60, 70, 80},
    {90, 99}
}
"""
# List of list
# 3D
"""large_data = [
    [
        [10, 20, 30],
        [40, 50, 60, 70, 80],
        [90, 99]
    ],
    [
        [10, 20, 30],
        [40, 50, 60, 70, 80],
        [90, 99]
    ]
]"""
"""
error in 3D list for set 
"""
large_data = (
    (
        (10, 20, 30),
        (40, 50, 60, 70, 80),
        (90, 99)
    ),
    (
        (10, 20, 30),
        (40, 50, 60, 70, 80),
        (90, 99)
    )
)
# 1. Indexing -> get only one elemmnt
print(len(my_data))
print(my_data[1])
# indexing is all abount the numbers i.e. 0 , 1 , 2

print(len(numbers))  # 3
print(numbers[1])  # [40, 50, 60, 70, 80]
print(numbers[1][2])  # 60

print(large_data[1][2][0])  # 90's
# 1 pixel -> list


# -----------------
# 2. Negative indexing
print(my_data[-1])  # 30
# 2D Negative indexing
print(numbers[-2][-1])  # 80
# 3D Negative indexing
print(large_data[-1][-2][-3])  # 60

# ----------------------------------------------------
# SLICING -> print many elements ->picking elements from the list an
# INTERVIEW QUES
# data = list(range(10, 101, 10))
data = tuple(range(10, 101, 10))
# data = set(range(10, 101, 10))-> ERROR IN set in slicing
print(data)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# to pick few elements
print("data[0:5] : ", data[0:5])  # 0 t0 less than 5  ---> OR ---> data[:5]
print("data[6:] : ", data[6:])  # data[6:] :  [70, 80, 90, 100]
print("data[5:9] : ", data[5:9])  # data[5:9] :  [60, 70, 80, 90]
print("data[:-5] : ", data[:-5])  # data[:-5] :  [10, 20, 30, 40, 50]
print("data[-5:-2] : ", data[-5:-2])  # data[-5:-2] :  [60, 70, 80]
print("data[-5:] : ", data[-5:])  # data[-5:] :  [60, 70, 80, 90, 100]

# -------------------
# Concatenation
# List:->
# data1 = [10, 20, 30]
# data2 = [40, 50, 60]
# tuple:->
data1 = (10, 20, 30)
data2 = (40, 50, 60)
# Set:->
# data1 = {10, 20, 30}
# data2 = {40, 50, 60          -> error in set in concatenation
data3 = data1 + data2
print("data3:", data3)  # dono merge ho gyi
# concatenation on paytm


# ----------------
# Multiplicity -> multiply your list 2-> means doubling the list
data4 = data1 * 2
print(data4)  # [10, 20, 30, 10, 20, 30]
# dishes to add on carrt


# ---------------
# Membeship testing -> true / false
# it works for set, tuple, list
print(100 in data1)
print(10 in data1)
print(100 not in data1)

# dictionary:->
Student = {
    "name": "Sukhmani",
    "age": "19",
    "gender": "Female",
    "roll_no": 101
}
Student2 = {
    "name": "Sukhmani",
    "age": "19",
    "gender": "Female",
    "roll_no": 101
}
# student3 = Student2 + Student -> error of dict in concatenation
print()
print(Student["name"])
print("roll_no" in Student)

# Assignmwnt-> explore all the properties on string
quote = "Search the candle rather than cursing teh darkness"
print(quote[0])
print(quote[6])

print(quote[-8])
# d

print("quote[:5]", quote[:5])
# quote[:5] Searc

quote1 = "Search the candle rather than cursing teh darkness"
quote3 = quote1 + quote
print("Concatemation ", quote)
# Concatemation  :Search the candle rather than cursing teh darkness

quote4 = quote *2
print("Multiplicity:", quote4)
# Multiplicity: Search the candle rather than cursing teh darknessSearch the candle rather than cursing teh darkness

# Membeship testing -> true / false
print("Search" in quote1)
