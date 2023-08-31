#nesteed function - local function
# create func inside ohter finction

def outer():
    print("this is outer function")

    def inner(): # nested/local function
        print("this is inner function")

    # inner()
    print("this is inner", inner)
    return inner

# outer()
# here if we cll inner function it will not execute because inner is the part of outer
# so it will inly be called inside the outer function
result = outer()
print("result is:", result)
result() # here the hashcode of the inner is same as that of the result
