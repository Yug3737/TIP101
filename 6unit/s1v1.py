
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
    


# edge cases
head = None
print(is_palindrome(head))

head1 = Node(1, Node(2, Node(1, Node(1))))
print(is_palindrome(head1))