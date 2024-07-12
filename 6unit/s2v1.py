class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_loop_start(head, meeting_point):
    slow = head
    fast = meeting_point

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# # Time = O(n + n) = O(200n) = O(n)
# # Space = O(1)
# def is_circular(head):
#     if not head:
#         return False
#     curr = head
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             break
        

#     if slow == fast:
#         start = find_loop_start(head, fast)
#         if start == head:
#             return True
#         else:
#             return False

#     return False

# head = Node(1, Node(2, Node(3, Node(4))))
# head.next.next.next.next = head.next
# print(is_circular(head))

# # 1 -> 2 -> 3 ->4 -> back at 2

# Planning
# Use fast and slow ptr to detect cycle
# After that find start of cycle
# From the start of cycle start traversing the cycle and stop 
# where current.next == start, we stop
# return the obj that current is pointing to    

# def find_last_node_in_cycle(head):
#     if not head:
#         return False
#     curr = head
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             break


#     if slow == fast:
#         start = find_loop_start(head, fast)
#         curr = start.next
#         while curr.next != start:
#             curr = curr.next
#         return curr.value
    


# # num1 -> num2 -> num3 -> num4 -> num2
# head = Node(1, Node(2, Node(3, Node(4))))
# head.next.next.next.next = head
# print(find_last_node_in_cycle(head)) # expect num4

# # 1 -> 2 -> back to the same 1
# # cycle starts at?? 1
# # return 2

# head = Node(1, Node(2))
# head.next.next = head
# print(find_last_node_in_cycle(head)) # expect 2

# head = None
# print(find_last_node_in_cycle(head)) # expect False

def partition(head, val):
    pass

# Planning 
# tempHead -> head(1) -> 4 -> 3 -> 2 -> 5 -> 2
#
#
# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# 1 -> 2 -> 3 -> 4 -> 5 -> 2
# 1 -> 2 -> 2 -> 4 -> 5 -> 3
# Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 
    #                 2 -> 2 -> 1 -> 5 -> 4 -> 3
    