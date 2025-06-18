


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, data):
        #create new node using Node class
        new_node = Node(data)

        #check if empty list then make the new node head if the list is empty
        if self.head is None:
            self.head = new_node
            return

        #travese through the list
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def delete(self, ddata):
        curr = self.head
        if self.head is None:
            print("Nothing to delete sir")
            return

        if self.head == ddata:
            self.head = self.head.next
            return







    def display(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(' -> '.join(elements))

#=======================================================================================================================
if __name__ == "__main__":
    head = SinglyLinkedList()
    head.append(2)
    head.append(4)
    head.append(6)
    head.append(8)
    head.prepend(1)
    head.prepend(0)
    head.delete(0)
    head.display()