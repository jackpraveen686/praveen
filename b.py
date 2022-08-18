
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
        

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.ref
ll=LinkedList()
n1=Node(2)
ll.head=n1
n2=Node(3)
n1.ref=n2
n3=Node(4)
n2.ref=n3
ll.print_LL()
