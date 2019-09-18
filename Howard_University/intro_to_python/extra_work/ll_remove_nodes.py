#Remove nodes greater than 100

import random

class Node:
    def __init__(self, val = None, nxt = None):
        self.val = val
        self.nxt = nxt

class LinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def append(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            self.tail.nxt = newNode
        self.tail = newNode

    def removeGreaterThan(self, val):
        curr_node = self.head
        prev_node = self.head

        while curr_node is not None:
            if curr_node.val > val:
                if curr_node == self.head: #Re-assigns everything to the first node of the LinkedList
                    self.head = curr_node.nxt
                    curr_node = curr_node.nxt
                    prev_node = curr_node
                elif curr_node != self.tail: #Previous node points to next node of the current node
                    prev_node.nxt = curr_node.nxt
                    curr_node = curr_node.nxt
                else:
                    prev_node.nxt = None #Since the last node is greater than val, prev_node.nxt = None
                    curr_node = None
            else:
                if curr_node == self.head:
                    curr_node = curr_node.nxt
                elif curr_node != self.tail:
                    prev_node = prev_node.nxt
                    curr_node = curr_node.nxt
                else:
                    curr_node = curr_node.nxt


    def printLinkedList(self):
        string = "Nodes: "
        temp = self.head

        while temp is not None:
            string += str(temp.val) + " "
            temp = temp.nxt

        print(string)

linkedlist = LinkedList()
array = [random.randint(1, 200) for _ in range(5)] #_ is aa "throw away" variable
for i in array:
    linkedlist.append(i)

print(str(array))
linkedlist.removeGreaterThan(100)
linkedlist.printLinkedList()
