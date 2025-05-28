class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self, val):
        return str(self.val)


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

def value_check(head, target):
    curr = head
    while curr:
        if curr.val == target:
            return True
        curr = curr.next
    return False

def length_of_list(head):
    curr = head
    length = 0
    while curr:
        if curr.val != 0:
            length += 1
            curr = curr.next
    return length

def delete_node(head, pos):
    curr = head
    prev = None
    if pos == 0:
        head = curr.next
        return head

    for i in range(0, pos):
        prev = curr
        curr = curr.next

    prev.next = curr.next
    return head






if __name__ == "__main__":
    head = SinglyNode(1)
    head.next = SinglyNode(2)
    head.next.next = SinglyNode(3)
    head.next.next.next = SinglyNode(4)
    head.next.next.next.next = SinglyNode(5)
    head = delete_node(head, 4)
    display(head)




