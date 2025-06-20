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
        #case 1: the deleted data is the head
        if self.head == ddata:
            self.head = self.head.next
            return

        #case 2: handle empty list
        if self.head is None:
            print("The list is empty, so what are you deleting!")
            return

        #case 3: normal traversal through the list
        curr = self.head
        prev = None
        while curr and curr.data != ddata:
            prev = curr
            curr = curr.next

        #case 3.1: number is not in the list
        if curr is None:
            print("the number you want to delete is nowhere to be found in the fucking list mate!")
            return
        #case 3.2: found the number
        prev.next = curr.next
        curr.next = None

    def add_node_at_pos(self, adata, pos):
        new_node = Node(adata)

        #case 1: list is empty
        if self.head is None:
            self.head = new_node
            return

        #case 2: add to 1st node -> prepend
        if pos == 0: #0-indexed
            self.prepend(adata)
            return

        #case 3: traversal through the list
        prev = None
        curr = self.head
        curr_idx = 0
        while curr and curr_idx < pos:
            prev = curr
            curr = curr.next
            curr_idx += 1

        if prev is None:
            print(f"Cannot add at position {pos}. List is empty or position is invalid.")
            return

        if curr is None and curr_idx < pos:
            print("the position is beyond the list size")
            return

        prev.next = new_node
        new_node.next = curr


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
    head.add_node_at_pos(1, 2)

    head.display()