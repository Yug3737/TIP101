def circular_list_length(head):

    # Linear Solution with Hashing
    # Better with Flyod

    # detecting looping point
    slow, fast = head, head
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # slow and fast are both at same place now
    count = 1
    slow = slow.next
    while slow != fast:
        count += 1
        slow = slow.next
    return count

head = Node(1,Node(2, Node(3)))
head.next.next.next = head
print(circular_list_length(head)) # expect 3 