class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

def delete_node(head, pos):
    curr = head
    prev = None
    if pos == 0:
        return head.next
    for i in range(0, pos):
        prev = curr
        curr = curr.next
    prev.next = curr.next
    return head



if __name__ == "__main__":

    head = SinglyNode(1)
    head.next = SinglyNode(2)
    head.next.next = SinglyNode(3)
    head = delete_node(head, 1)

    display(head)

