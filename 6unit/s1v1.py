
class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next
        
# S1 VERSION 1
def find_middle_element(head):
    if head is None:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def is_palindrome(head):
    if head is None or head.next is None:
        return True

# Finding the Middle element of LL
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Now slow is at the middle of Odd LL and 
    # at 2nd middle of even LL
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node
    
    left, right = head, prev
    while right:
        if right.val != left.val:
            return False
        left = left.next
        right = right.next
    return True
    