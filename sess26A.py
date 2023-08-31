# FUnction as Input
# i.e passifn the function by refernce
def show(func):
    print("show executed")
    func()


def hello():
    print("this os hello")
    print("hello finished")


def bye():
    print("this is bye")
    print("bye function finished")


show(hello)
print("--------------------")
show(bye)
