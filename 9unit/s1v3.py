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