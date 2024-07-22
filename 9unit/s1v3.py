# BFS / Level Order Traversal Iterative
from collections import deque

class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    queue = deque()
    if root:
        queue.append(root)
    level = 0
    while len(queue) > 0:
        print("level:",level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


root = TreeNode(19, TreeNode(7, TreeNode(5, None, TreeNode(6)), None), TreeNode(25, TreeNode(22), TreeNode(71, TreeNode(30), TreeNode(96))))
# print(bfs(root))

def evaluate_tree(root):
    if not root:
        return 0

    if not root.left and  not root.right:
        return root.val
    
    leftVal = evaluate_tree(root.left)
    rightVal = evaluate_tree(root.right)

    if root.val == '+':
        return leftVal + rightVal
    elif root.val == '-':
        return leftVal - rightVal
    elif root.val == '*':
        return leftVal * rightVal
    else:
        return leftVal / rightVal

root = TreeNode('+',TreeNode('-', TreeNode(10), TreeNode(5)), TreeNode('*', TreeNode(2), TreeNode(3)))
print(evaluate_tree(root))


# this solution only works if all the values in the original tree are unique
# def get_target_copy(original, cloned, target):

#     def dfs(node):
#         if not node:
#             return None
#         elif node.val == target.val:
#             return node
        
#         return dfs(node.left) or dfs(node.right)
    
#     return dfs(cloned)

def get_target_copy(original, cloned, target):

    def dfs(originalNode, clonedNode):
        if not originalNode:
            return None
        elif originalNode == target:
            return clonedNode
        else:
            return dfs(originalNode.left, clonedNode.left, target) or dfs(originalNode.right, clonedNode.right, target)
        
    dfs(original, cloned)

def has_path_sum(root, target_sum):
    if not root:
        return False
    if not root.right and not root.left:
        return root.val == target_sum 
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)

# 1) Base case: If the current node is None, return False.
# 2) Check if the current node is a leaf (no children) and if its value equals target_sum.
# 3) Recursively check the left and right subtrees with the updated target_sum (subtract the current node's value from target_sum).
# 4) Return True if either subtree has a valid path, otherwise return False.
print("here")
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(root, 5) # returns false
#       5
#      / \
#     4   8
#    /   / \  
#   11  13  4
#  / \       \
# 7   2       1
root = TreeNode(5,TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print(has_path_sum(root, 22)) # expect Treu