# Bitwise Operators
# &, |, ^

num1 =  10
num2 = 8

# to print the numbers in binary form
print(f"{num1} binary : {bin(num1)}")
print(f"{num2} binary : {bin(num2)}")

result1 = num1 & num2
print(f"Result1 is : {result1} and binary is {bin(result1)}")

result2 = num1 | num2
print(f"Result2 is {result2} and binary is {bin(result2)}")
# 8 4 2 1
# 1 0 1 0 ->10
# 1 0 0 0 ->8
# result3 = num1 ^ num2
# print( f" Result3 is {result3} and bianry is {bin(result3)}")

# shift operators | for security purpose
# >> <<
# >>--> right shift
#  <<--> left shift

num1 = 8
num2 = 2

result1 = num1 >> num2 #-> num1/num2
result2 = num1 << num2 #-> num1 ki power num2
result3 = result2 >> num2
print(f"Result1 is : {result1} and binary is {bin(result1)}")
print(f"Result2 is : {result2} and binary is {bin(result2)}")
print(f"Result3 is : {result3} and binary is {bin(result3)}")

num3 = 11
result4 = num3 >> 2
print(f"Result4 is : {result4} and binary is {bin(result4)}")

# binary of 11 is ->  1 0 1 1
#                     _ _ 1 0 -> 0 0 1 0 -> 2


num3 = -11
result5 = num3 >> 2
print (f"Result5 is : {result5} and binary is {bin(result5)}")


"""
 binary of -11           -> 1 0 1 1
1's compliments of 11 is -> 0 1 0 0 
2's compliments of 11 is -> 0 1 0 0
                                + 1
                         -> 0 1 0 1
0 1 0 1 >> 2 
_ _ 0 1 -> 1 1 0 1
1's compliment  -> 0 0 1 0 
2's compliments -> 0 0 1 0 
                       + 1 
                   _______
                   0 0 1 1 -> -3
"""
# Right shift -13 by 3
"""
binary of 13-> 1 1 0 1
1's compliments of 13 is -> 0 0 1 0
2's compliments of 13 is -> 0 0 1 0 
                                + 1 
                            0 0 1 1 
0 0 1 1 >> 3
_ _ _0 -> 1 1 1 0 


1's compliments of 13 is -> 0 0 0 1
2's compliments of 13 is -> 0 0 0 1
                                + 1 
                            0 0 1 0 
 ANSWER is -> -2 
"""

