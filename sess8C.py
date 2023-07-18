# shuffle algo of linked list
# from random import randint
#
#
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#     def shuffle(self):
#         nodes = []
#         current = self.head
#         while current:
#             nodes.append(current)
#             current = current.next
#
#         shuffled_nodes = []
#         while nodes:
#             index = randint(0, len(nodes) - 1)
#             shuffled_nodes.append(nodes.pop(index))
#
#         self.head = shuffled_nodes[0]
#         current = self.head
#         for i in range(1, len(shuffled_nodes)):
#             current.next = shuffled_nodes[i]
#             current = current.next
#         current.next = None
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         print()
#
#
# # Create a LinkedList instance
# linked_list = LinkedList()
#
# # Add elements to the linked list
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.append(5)
#
# # Display the original linked list
# print("Original Linked List:")
# linked_list.display()
#
# # Shuffle the linked list
# linked_list.shuffle()
#
# # Display the shuffled linked list
# print("Shuffled Linked List:")
# linked_list.display(
#

import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            new_node.prev = last_node
            new_node.next = self.head
            last_node.next = new_node
            self.head.prev = new_node

    def shuffle(self):
        if self.head is None:
            return

        # Convert circular doubly linked list to regular doubly linked list
        last_node = self.head.prev
        last_node.next = None

        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next

        # Shuffle the nodes in the regular doubly linked list
        random.shuffle(nodes)

        # Convert the shuffled doubly linked list to circular doubly linked list
        self.head = nodes[0]
        current = self.head
        for i in range(1, len(nodes)):
            current.next = nodes[i]
            current.next.prev = current
            current = current.next

        last_node = current
        last_node.next = self.head
        self.head.prev = last_node

    def display(self):
        if self.head is None:
            return

        current = self.head
        while True:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()


# Create a circular doubly linked list instance
cdll = CircularDoublyLinkedList()

# Add elements to the circular doubly linked list
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(4)
cdll.append(5)

# Display the original circular doubly linked list
print("Original Circular Doubly Linked List:")
cdll.display()

# Shuffle the circular doubly linked list
cdll.shuffle()

# Display the shuffled circular doubly linked list
print("Shuffled Circular Doubly Linked List:")
cdll.display()
