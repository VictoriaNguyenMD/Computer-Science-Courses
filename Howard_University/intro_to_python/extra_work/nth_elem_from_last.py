#For a Singly Linked List, find the nth to last element (Problem 8) and re-arrange the linked list eg. 123456 --> 162534
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

    def length(self):
        curr_node = self.head
        counter = 0

        while curr_node is not None:
            counter += 1
            curr_node = curr_node.nxt
        return counter

    def nth_to_last_element(self, nth_element):
        # nth_element = int(input("Write the nth position from the last element: ")) - 1
        nth_element = nth_element - 1
        counter = 1
        curr_node = self.head
        loops = self.length() - nth_element

        if loops <= 0:
            return ("This position is not valid.")
        else:
            while counter != loops:
                counter += 1
                curr_node = curr_node.nxt

            return curr_node.val


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

linkedlist.printLinkedList()

new_linkedlist = LinkedList()

def rearrange():  # 0123456 becomes 0615243
    temp_for = linkedlist.head
    num_rev = 1
    temp_rev_val = linkedlist.nth_to_last_element(num_rev)

    alternate = 1
    while temp_for.val != temp_rev_val:
        if alternate % 2 != 0:
            new_linkedlist.append(temp_for.val)
            temp_for = temp_for.nxt
        else:
            new_linkedlist.append(temp_rev_val)
            num_rev += 1
            temp_rev_val = linkedlist.nth_to_last_element(num_rev)
        alternate += 1

    if temp_for.val == temp_rev_val:
        new_linkedlist.append(temp_for.val)

print("\n")
nth = int(input("What element from the last do you want to see?"))
print("Nth to last element: " + str(linkedlist.nth_to_last_element(nth)))

rearrange()
print("\n")
print("Re-arrange the nodes: ")
new_linkedlist.printLinkedList()


