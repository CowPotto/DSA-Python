class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_llist(arr) -> ListNode:
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def llist_to_list(head) -> list:
    curr = head
    arr = []
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

def llist_display(head) -> None:
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        while l1 or l2 or carry:
            if l1 is not None:
                val1 = l1.val
            else:
                val1 = 0

            if l2 is not None:
                val2 = l2.val
            else:
                val2 = 0

            sum_val = val1 + val2 + carry
            digit = sum_val % 10
            carry = sum_val // 10
            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next

if __name__ == "__main__":
    # Correction: Instantiate the Solution class
    s = Solution()

    print("--- Test Case 1 ---")
    list_1 = [1, 2, 3] # Represents 321
    list_2 = [4, 5, 6] # Represents 654
    llist_1 = list_to_llist(list_1)
    llist_2 = list_to_llist(list_2)
    print("Input List 1:", list_1)
    print("Input List 2:", list_2)
    print("Linked List 1 (visual): ", end="")
    llist_display(llist_1)
    print("Linked List 2 (visual): ", end="")
    llist_display(llist_2)

    result_llist = s.addTwoNumbers(llist_1, llist_2)
    print("Result Linked List (visual): ", end="")
    llist_display(result_llist)
    print("Result as List:", llist_to_list(result_llist)) # Expected: [5, 7, 9] (975)
    print("-" * 20)

    print("--- Test Case 2: Different Lengths with Carry ---")
    list_3 = [9, 9] # Represents 99
    list_4 = [9, 9, 9] # Represents 999
    llist_3 = list_to_llist(list_3)
    llist_4 = list_to_llist(list_4)
    print("Input List 1:", list_3)
    print("Input List 2:", list_4)
    print("Linked List 1 (visual): ", end="")
    llist_display(llist_3)
    print("Linked List 2 (visual): ", end="")
    llist_display(llist_4)

    result_llist_2 = s.addTwoNumbers(llist_3, llist_4)
    print("Result Linked List (visual): ", end="")
    llist_display(result_llist_2)
    print("Result as List:", llist_to_list(result_llist_2)) # Expected: [8, 9, 0, 1] (1098)
    print("-" * 20)

    print("--- Test Case 3: Final Carry ---")
    list_5 = [9] # Represents 9
    list_6 = [9] # Represents 9
    llist_5 = list_to_llist(list_5)
    llist_6 = list_to_llist(list_6)
    print("Input List 1:", list_5)
    print("Input List 2:", list_6)
    print("Linked List 1 (visual): ", end="")
    llist_display(llist_5)
    print("Linked List 2 (visual): ", end="")
    llist_display(llist_6)

    result_llist_3 = s.addTwoNumbers(llist_5, llist_6)
    print("Result Linked List (visual): ", end="")
    llist_display(result_llist_3)
    print("Result as List:", llist_to_list(result_llist_3)) # Expected: [8, 1] (18)
    print("-" * 20)


