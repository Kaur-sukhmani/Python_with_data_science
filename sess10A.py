from sess10 import ScreenInterface, Stack


def main():
    interface1 = ScreenInterface(title="Home page")
    interface2 = ScreenInterface(title="Product 1 Page")
    interface3 = ScreenInterface(title="Product 2 Page")
    interface4 = ScreenInterface(title="Product 3 Page")

    stack = Stack()

    stack.push(interface1)  # head
    stack.push(interface2)
    stack.push(interface3)  # tail

    stack.pop()
    stack.pop()
    stack.pop()

    stack.push(interface4)
    stack.push(interface1)
    stack.push(interface3)

    stack.iterate()
    print("Stack:", vars(stack))


if __name__ == "__main__":
    main()
