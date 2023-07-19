# args and kwargs
# *args -> Multiple/variable arguments can be passed as tuple
def add(*args):
    print(args)
    print(type(args))


add(30, 50)
add(10, 20, 30, 50)
add(10.2, 32.6, 23.5)


# **kwargs -> keyword arguments
def employee(**kwargs):
    print(employee)
    print(type(kwargs))


employee(name="Sukhmani", emp_id=231)


def fun(*args, **kwargs):
    print(args)
    print(kwargs)


fun(10, 20, 30, "John", "Sia", name="harry", age=10)
