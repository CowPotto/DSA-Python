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

def add_node_at_beginning(head, val):
    curr = head
    new_node = SinglyNode(val)
    new_node.next = head
    head = new_node
    return head

def add_node_at_end(head, val):
    curr = head
    new_node = SinglyNode(val)
    while curr.next:
        curr = curr.next

    curr.next = new_node

    return head

def list_length(head):
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    return count

def remove_dup(head):
    if not head:
        return None

    curr = head
    prev = None
    seen = set()
    while curr:#must revise
        if curr.val in seen:
            if prev:
                prev.next = curr.next
            else:
                pass
        else:
            seen.add(curr.val)
            prev = curr
        curr = curr.next
    return head

if __name__ == "__main__":

    head = SinglyNode(1)
    head = add_node_at_end(head, 2)
    head = add_node_at_end(head, 3)
    head = add_node_at_end(head, 5)
    head = add_node_at_end(head, 5)

    head = remove_dup(head)
    display(head)

