class ScreenInterface:
    def __init__(self, title=""):
        self.title = title
        self.next = None
        self.previous = None

    def show(self):
        print(">> {}".format(self.title))


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # same as circular doubly ;inked list
    def push(self, interface):
        self.size += 1

        if self.head is None:
            self.head = interface
            self.tail = interface
        else:
            self.tail.next = interface
            interface.previous = self.tail

            # Any newly added interface will be tail :)
            self.tail = interface
            self.tail.next = None

    def iterate(self):
        # backward iteration
        if self.size != 0:
            temp = self.tail
            while temp is not None:
                temp.show()
                temp = temp.previous

                if temp == self.tail:
                    break

    def pop(self):
        if self.size != 0:
            self.size -= 1
            self.tail = self.tail.previous

            if self.tail is None:
                self.head = None
        else:
            print("Stack is empty:")
