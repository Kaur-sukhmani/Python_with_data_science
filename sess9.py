def compute_taxes(amount, tax):
    amount_to_pay = amount + amount*tax
    return amount_to_pay

# Hashcode is printed
print("compute_taxes is:", compute_taxes)
# compute_taxes is: <function compute_taxes at 0x102cbc540>
print("compute_taxes hashcode is:", id(compute_taxes), hex(id(compute_taxes)))

# Reference copy:)
fun = compute_taxes
print("Fun is :", fun)
# Fun is : <function compute_taxes at 0x102950540>

result = fun(amount=100, tax=0.18)
print("Result is:", result)
# Result is: 118.0

# if we delete compute_taxes then
del compute_taxes

result = fun(amount=200, tax=0.18)
print("Result is:", result)
# the point is even if we delete the result will be the fun

result = fun(100, 18)


