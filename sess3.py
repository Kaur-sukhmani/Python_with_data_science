"""
   session 3
   CONTROLLER
      operators             -> Mathematical Computations
      conditional instructs -> Decision making
      Loops/iterations      -> Repetition
 """

#operators
# Arithmatic Operators
# +, -, /, // ,* , **, %
Product_price = 125.25
taxes = 0.18
# Associativity and precedence of operators
price_to_pay = Product_price + (Product_price * taxes)
print(f"price to pay :\u20b9{price_to_pay}")

number = 10
result = number/3 #Floating point division
result2 = number // 3 #Integral division
print("Result:",result)
print("Result2:",result2)

base = 2
result = base * 3
print("Result3:",result)

result4 = base ** 3 #** means raise to power
print("Result4:",result)

# Assignment operator
# =,+=, -=, *=, **=, /=, //=, %=
age = 20
# age = age + 3
age += 3 #Shorthand operation
age += 10
age -= 5
age %= 3
print ("age is :",age )

# Increment and decrement operators
# ++ and -- operators does not exist in python

idx = 0
idx += 2
idx -= 1
print("idx is:",idx)








