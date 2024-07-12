class Node:
    def __init__(self, value, next= None) -> None:
        self.value = value
        self.next = next
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# def circular_list_length(head):

#     # Linear Solution with Hashing
#     # Better with Flyod

#     # detecting looping point
#     slow, fast = head, head
#     while slow != fast:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             break

#     # slow and fast are both at same place now
#     count = 1
#     slow = slow.next
#     while slow != fast:
#         count += 1
#         slow = slow.next
#     return count

# head = Node(1,Node(2, Node(3)))
# head.next.next.next = head
# print(circular_list_length(head)) # expect 3 


# def detect_and_remove(head): 
#     # detecting cycle using Tortoise and Hare
#     slow = fast = head
#     while fast != slow:
#         slow = slow.next
#         fast = fast.next.next

#     # slow and fast are at Node of Intersection
#     if not fast or not fast.next:
#         # means, fast and slow are at end of LL and cycle does not exist
#         return head

#     # finding start Node of cycle
#     slow2 = head
#     while slow != slow2:
#         slow = slow.next
#         slow2 = slow2.next
#     # slow and slow2 are at start of cycle now
#     # Now we move fast until it reaches the last Node before start of cycle

#     while fast.next != slow:
#         fast = fast.next

#     fast.next = None
#     return head

# head = Node(1, Node(2, Node(3)))
# head.next.next.next = head

# detect_and_remove(head)
# print_list(head)

# For input: 1 -> 2 -> 3 -> back to 1, we want just 1 -> 2 -> 3 -> None
# If cycle does not exist, return same LL

# O(n) space and O(n) time solution
def merge_two_lists(head_a, head_b):
    tempHead = Node(0)

    curr_a, curr_b = head_a, head_b
    temp_curr = tempHead
    while curr_a and curr_b:
        if curr_a.value <= curr_b.value:
            temp_curr.next = Node(curr_a.value)
            curr_a = curr_a.next
            temp_curr = temp_curr.next

        else:
            temp_curr.next = Node(curr_b.value)
            curr_b = curr_b.next
            temp_curr = temp_curr.next

    # Since we are outside, one of the list got exhausted
    while curr_a:
        temp_curr.next = Node(curr_a.value)
        temp_curr= temp_curr.next
        curr_a = curr_a.next

    while curr_b:
        temp_curr.next = Node(curr_b.value)
        temp_curr = temp_curr.next
        curr_b = curr_b.next
    
    return tempHead.next
            

# edge cases
# LL1 : 1 -> 2, LL2: -> 1 -> 3
# Result: 1 -> 1 -> 2 -> 2
ll1 = Node(1, Node(2))
ll2 = Node(1, Node(3))
result = merge_two_lists(ll1, ll2)
print_list(result)

# empty ll1, and another list
ll1 = None
result = merge_two_lists(ll1, ll2)
print(result) # expect same ll2