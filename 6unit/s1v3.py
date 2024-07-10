class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# problem 6
def reverse(head):
    prev, curr = None, head
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev