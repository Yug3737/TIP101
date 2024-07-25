from collections import deque

# class TreeNode:

#     def __init__(self, value=0, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

'''from collections import deque  # This is a popular library used for queues



def print_by_level(root):
    # If the tree is empty:
    # return
    if not root:
        return
    # Create an empty queue using deque
    queue = deque()
    # Add the root to the queue
    queue.append(root)
    # While the queue is not empty:
    while queue:
        qlen = len(queue)
        # for _ in range(qlen):
            # Pop the next node off the queue (pop from the left side!)
        node = queue.popleft()
        # Print the popped node
        print(node.val)
        # Add each of the popped node's children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
# print_by_level(root)
# BFS Algo
# Level Order Traversal
#     4
#    / \
#   2   6
#  / \
# 1   3
# Print
# 4, 2,6, 1 ,3
#   1 
#    \
     # 2
     #  \ 
     #   3'''

'''def level_sum(root):
    if not root:
        return []

    q = deque()
    q.append(root)
    sum = [] 

    while q:
        qlen = len(q)
        currSum = 0
        
        for _ in range(qlen):
            node = q.popleft()
            currSum += node.val
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        sum.append(currSum)

    return sum

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))

# print(level_sum(root))
  #     4 -> 4
  #    / \
  #   2   6 -> 8
  #  / \  
  # 1   3 -> 4'''

'''class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_max(root):
    queue = deque()
    if not root:
        return 0
    if root:
        queue.append(root)
    maxNodes = 1
    while queue:
        qlen = len(queue)

        for _ in range(qlen):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        currSize = len(queue)
        if currSize > maxNodes:
            maxNodes = currSize
    return maxNodes

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(7), TreeNode(8)))
# print(level_max(root))

root = TreeNode(1)'''
# # print(level_max(root))

# 1) If the tree is empty, return an empty list.
# 2) Create a dictionary to hold the nodes at each column index.
# 3) Create an empty queue and add the root node with column index 0.
# 4) While the queue is not empty:
#     a) Pop the next node and its column index from the queue.
#     b) If the node is not None, add its value to the dictionary at the corresponding column index.
#     c) Enqueue the left child with column index - 1.
#     d) Enqueue the right child with column index + 1.
# 5) Sort the dictionary keys (column indices) and extract the values in the sorted order.
# 6) Return the list of values.
from collections import defaultdict, deque

def vertical_order(root):
    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque()

    while queue:
        column = queue.popleft()

    if node:
        column_table[column].append(node.val)

        queue.append(node.left, column - 1)
        queue.append(node.right, column + 1)

sorted_columns = sorted(column.keys())  


# preorder = curr, left, right = 3, 9, 20, 15, 7
# inorder = left, curr, right = 9, 3, 15, 20, 7
# postorder = 9, 15, 7, 20 ,3
# [[9],[3,15],[20],[7]]
    
#         3
#        / \
#       9   20
#           / \
#          15  7
