
# # UNIT9

# # Problem 1: Is Symmetric Tree
# # Given the root of a binary tree, return True if the tree’s left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). Return False otherwise.

# # Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque
# def is_symmetric(root):
#   # q = deque()
#   # level = 0
#   # if root:
#   #   q.append(root)
#   # while len(q) > 0:
#   #   # Analyze our queue
#   #   qlen = len(q)
#   #   left, right = 0, qlen -1
#   #   while left < right:
#   #     if q[left] != q[right]:
#   #       return False
#   #     left += 1
#   #     right -= 1

#   #   for _ in range(qlen):
#   #     curr = q.popleft()
#   #     print(curr.val)
#   #     if curr.left:
#   #       q.append(curr.left)
#   #     if curr.right:
#   #       q.append(curr.right)
    
#   #   level +=1
#   #   return True
#   ######
#   # def isMirror(t1, t2):
#   #   if not t1 and not t2:
#   #     return True
#   #   if not t1 or not t2:
#   #     return False
#   #   return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t2.left, t1.right)

#   # if not root:
#   #   return True
#   # return isMirror(root.left, root.right)
#   if not root:
#     return True 
    
#   if root.left.val != root.right.val:
#     return False 

#   # Make Dry Run
#   # isSYMM(5)
#   # isSYMM(2) and isSYMM(2)
#   #     1
#   #    / \
#   #   2   2
#   # /  \
#   # 3   3
#   return is_symmetric(root.left) and is_symmetric(root.right)
  
# root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(3)), TreeNode(2))
# print(is_symmetric(root))

# # WE should recursively search left and right subtrees and make sure that our pointers point to nodes wiht same value
# # print(is_symmetric(None)) # returns True
# # root = TreeNode(1, TreeNode(2), TreeNode(3)) # returns False
# # print(is_symmetric(root))

# # root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
# # print(is_symmetric(root))

# # DFS solution
# # [1]
# # [2,2] BFS queue
# # [3,4,4,3] # check if our queue/arr is symmetric from both ends
# # O(n * logn)
#  #       1
#  #     /   \
#  #    /     \
#  #   2       2
#  #  / \     / \
#  # 3   4   4   3

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def binary_tree_paths(root):
  if not root:
    return []

  paths = []
  def dfs(node, path):
    if not node:
      return

    path.append(str(node.val))

    if not node.left and not node.right:
      paths.append("->".join(path))

    if node.left:
      dfs(node.left, path[:]) # copy of current path
    if node.right:
      dfs(node.right, path[:]) # copy of current path
  
  dfs(root, [])
  return paths

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(binary_tree_paths(root))
# inorder : left, curr, right
# 1 -> 2 -> 5
  #   1
  #  / \
  # 2   3
  #  \  
  #   5