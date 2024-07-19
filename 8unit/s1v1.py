class TreeNode():
     def __init__(self, value=0, left=None, right=None):
        # self.key = key
        self.value = value
        self.left = left
        self.right = right

def search_bst(node,key):
    # Base case: node is None or we find the key
    if node is None or node.key == key:
        return node

    # Recursive case, if current node's key is greater than desired, go left 
    if key < node.key:
        return search_bst(node.left, key)
    # else go right
    return search_bst(node.right, key)
    

# Problem 1

node4 = TreeNode(4)
node10 = TreeNode(10)
node6 = TreeNode(6)

node10.left = node4
node10.right = node6

# Nested Constructors
node10 = TreeNode(10, TreeNode(4), TreeNode(6))

# Problem 2
# def check_tree(root):
# 	return root.value == (root.left.value + root.right.value)

#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False
root = TreeNode(5, TreeNode(3), TreeNode(1))
# print(check_tree(root))

def check_tree(root):
    if not root:
        return None
    # Finiding sum of children
    leftValue = rightValue = 0
    if root.left:
        leftValue = root.left.value
    if root.right:
        rightValue = root.right.value
    return root.value == (rightValue + leftValue)


#   5
#    \
#     2
# Input: root = 5
# Expected Output: False  5
root = TreeNode(5, TreeNode(3), TreeNode(2))
# print(check_tree(root))

# Problem 3
def left_most(root):
    # curr = root
    # while curr.left:
    #     curr = curr.left
    # return curr.value

    # Recursive Solution
    if not root:
        return None
    # BAse Case
    if not root.left:
        return root.value

    return left_most(root.left)

root = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4))))
# print(left_most(root))

def inorder_traversal(root):
    if not root:
        return None
    if root.left:
        inorder_traversal(root.left)
    print(root.value, end=', ')

    if root.right:
        inorder_traversal(root.right)

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5)), TreeNode(6))
# print(inorder_traversal(root))

def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5)), TreeNode(6))
# print(size(root))


def find(root, value):
    if not root:
        return False 
    if root.value == value:
        return True 
    
    return find(root.left, value) or find(root.right, value)


root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5)), TreeNode(6))
print(find(root, 5))

def bst_find(root,value):
    if not root:
        return False
    if root.value > value:
        bst_find(root.left, value)
    elif root.value == value:
        return True
    else:
        bst_find(root.right, value)

def collect_desc_leaves(root,leaves):
    if not root:
        return None
    collect_desc_leaves(root.right, leaves)

    if not root.right and not root.left:
        leaves.append(root.value)
    
    collect_desc_leaves(root.left, leaves)

def descending_leaves(root):
    leaves = []
    collect_desc_leaves(root,leaves)
    return leaves
#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: [5, 3, 1]
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(descending_leaves(root)) # expect [5,3,1]