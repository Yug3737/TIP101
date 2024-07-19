# class TreeNode():
#    def __init__(self, value, left=None, right=None):
#        self.val = value
#        self.left = left
#        self.right = right

# # Understand
# # all values same
# #  
# # Planning
# # grab root value and check if something different
# # postorder, preorder, inorder DFS traversal
# # preorder -> curr, left, right
# # inorder -> left, curr, right
# # postorder -> left, right, curr

# # Example Input Tree #1

# #       1
# #      / \
# #     /   \
# #     1   1
# #   / \     \
# #  1   1     1
# # # Ask interviewer
# def is_univalued(root):
#       if not root:
#          return True
#       checkVal = root.val
#       return helper(root, checkVal)
# def helper(root, checkVal):
# #   checkValue = root.value
#    if not root:
#       return True
#    if root.val != checkVal:
#       return False
#    # return something(node.left) and something(node.right)
#    # return is_univalued(rot.left) and is_univalued(root.right)
   
#    return helper(root.left, checkVal) and helper(root.right, checkVal)


# root = TreeNode(1, TreeNode(1, TreeNode(2)), TreeNode(1))
# print(is_univalued(root))
# # helper function to compare previous
# # Psuedocode
# # go to left subtree
# # check each node
# # if any node has different value, return False
# # if currNode has same value
# # visit left subtree and right subtree


# Given the root of a binary tree, write a function height() that returns the height of a binary tree.

# # Evaluate the time complexity of your function.
# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
        
# def height(root):
#    if not root:
#       return 0

   
#    left = height(root.left)
#    right = height(root.right)
#    return max(left, right) + 1

# # Idea of Plan
# # #     4 (2 + 1) -> 3
# #   2  / \ 1
# #     /   \
# #    2     5
# #   / \    
# #  1   3    

# # Input: root = 4
# # Expected Output: 3

# root = TreeNode(1, TreeNode(1, TreeNode(2)), TreeNode(1))
# print(height(root))

# Input: root = 10, key = 9, value = 'Naruto' 
# Expected Output: root = 10
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6
#       \
#        9    

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
         self.key = key
         self.val = value
         self.left = left
         self.right = right

def insert(root, key, value):
   if not root:
      return TreeNode(key, value)

   if key < root.key:
      root.left = insert(root.left, key, value)
   elif key > root.key:
      root.right = insert(root.right, key, value)
   else:
      root.val = value

   return root.val

#       10
#      /  \
#     /    \
#    8      15
#   / \    
#  1   6    

root = TreeNode(10, 'a',TreeNode(8, 'b', TreeNode(1, 'c'), TreeNode(6, 'd')), TreeNode(15, 'e'))
print(insert(root,9, "Naruto"))