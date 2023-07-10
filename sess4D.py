# f(x) = x*x + 1
# x=1
# f(1) = 1*1 + 1


# 1 way
"""
def f(x):
    result = x*x + 1
    print("result is:", result)

f(1)
f(2)
"""

# 2nd way
def f(x):
    return x*x + 1

result = f(1)
print("Result is:", result)
# OR
print("Result is:", f(2))
print("Result is:", f(3))
