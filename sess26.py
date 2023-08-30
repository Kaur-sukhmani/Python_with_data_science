# decorators
import datetime


def show():
    print("this is show")
    print("today is :", datetime.datetime.today())

# reference copy operation
hello = show

print("show is", show)
print("hello id ", hello)

show()
hello()
