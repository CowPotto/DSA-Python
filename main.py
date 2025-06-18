class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, data):
        #create new node using Node(data)
        new_node = Node(data)

        #if there is no node yet, the new node is the head
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        # traverse through the list until the curr.next = None, means that it is the last node
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        #the next pointer of new node point to head
        new_node.next = self.head
        #set the new node to current head
        self.head = new_node

    def display(self):
        curr = self.head
        if not curr:
            print("The list is empty!")
            return

        elements = []
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(' -> '.join(elements))

    def add_node_after(self, prev_node_data, new_data):
        if not self.head:
            print("the list is fucking empty")
            return

        found_prev_node = False
        curr = self.head
        while curr:
            if curr.data == prev_node_data:
                found_prev_node = True
                break
            curr = curr.next

        if not found_prev_node:
            print(f"there is no {prev_node_data} in the fucking list mate")
            return

        new_node = Node(new_data)
        new_node.next = curr.next
        curr.next = new_node

    def delete_node(self, specific_data):
        #Case 1: The number is nowhere to find in the list
        if not self.head:
            print("This fuccking list is empty, again!")
            return

        #Case 2: the number is the head node
        if self.head.data == specific_data:
            self.head = self.head.next
            return

        #Case 3: normal traversal to delete specific node using prev and curr technique
        prev = None
        curr = self.head
        while curr and curr.data != specific_data:
            prev = curr
            curr = curr.next

        if curr is None:
            print("you cannot delete a number that is not in the list you dumb fuck!")
            return

        prev.next = curr.next
        curr.next = None

#=======================================================================================================================

if __name__ == "__main__":
    head = LinkedList()
    head.append(5)
    head.append(7)
    head.append(9)
    head.prepend(3)
    head.add_node_after(9, 4)
    head.delete_node(4)
    head.delete_node(5)

    head.display()
