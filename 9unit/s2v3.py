
# level order traversal in dictionary
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

# Time O(n), What is the space complexity here? 
def level_dict(root):
    dict = {}
    queue = deque()
    val_queue = deque()
    level = 1

    if root:
        queue.append(root)
        val_queue.append(root.val)
    while queue:
        qlen = len(queue)
        dict[level] = list(val_queue)
        print("level", level)
        
        for _ in range(qlen):
            curr = queue.popleft()
            val_queue.popleft()
            print(curr.val, end=" ")
            if curr.left:
                queue.append(curr.left)
                val_queue.append(curr.left.val)
            if curr.right:
                queue.append(curr.right)
                val_queue.append(curr.right.val)
        level += 1
    return dict

# root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
# print(level_dict(root))

        
# def get_level_range(root, start_level, end_level):
#     result = []
#     level = 1
#     q = deque()
#     if root:
#         q.append(root)
#         if start_level <= level <= end_level:
#             result.append(root.val)
    
#     while len(q) >0:
#         qlen = len(q)

#         level +=1 
#         for _ in range(qlen):
#             curr = q.popleft()
#             if curr.left:
#                 q.append(curr.left)
#                 if start_level <= level <= end_level:
#                     result.append(curr.left.val)
#             if curr.right:
#                 q.append(curr.right)
#                 if start_level <= level <= end_level:
#                     result.append(curr.right.val)
            
#     return result


# #         3
# #        / \
# #       /   \
# #      /     \
# #     5       1
# #    / \     / \  
# #   6   2   0   8
# #      / \  
# #     7   4
# root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
# print(get_level_range(root, 2, 4))

def print_corner_nodes(root):
    if not root:
        return None
    q = deque()
    val_q = deque()
    q.append(root)
    val_q.append(root.val)

    while len(q) > 0:
        qlen = len(q)
        if val_q[0] == val_q[-1]:
            print("only one: ", val_q[0])
        print("first", val_q[0], "last", val_q[-1])

        for _ in range(qlen):
            curr = q.popleft()
            val_q.popleft()

            if curr.left:
                q.append(curr.left)
                val_q.append(curr.left.val)
            if curr.right:
                q.append(curr.right)
                val_q.append(curr.right.val) 
    
        print("types in val_q: ", [type(v) for v in val_q])
        
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
# print_corner_nodes(root)

def lca(root, p, q):
    curr = root
    
    while curr:
        if p. val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else: # either one of the nodes is equal to current or we have a split where
            # one node is greater than curr and other is less meaning curr is the LCA
            return curr 



def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + self.minDepth(root.right)
    if not root.right:
        return 1 + self.minDepth(root.left)
    
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) 

def level_difference(root):
    oddSum = evenSum = 0
    if not root:
        return 0
    q = deque()
    val_q = deque()
    q.append(root)
    val_q.append(root.val)
    level = 1
    while q:
        qlen = len(q)
        if level % 2 == 0:
            evenSum += sum(val_q)
        else:
            oddSum += sum(val_q)
        for _ in range(qlen):
            curr = q.popleft()
            val_q.popleft()

            if curr.left:
                q.append(curr.left)
                val_q.append(curr.left.val)
            if curr.right:
                q.append(curr.right)
                val_q.append(curr.right.val)
        level += 1
    return oddSum - evenSum

# root = TreeNode(6, TreeNode(3, TreeNode(5)), TreeNode(8, TreeNode(4, TreeNode(1), TreeNode(7)), TreeNode(2, None, TreeNode(3))))
# print(level_difference(root))

def find_tilt(root):
    
    def find_tilt_helper(root, sum):
        if not root:
            return sum
        leftSum = find_tilt_helper(root.left, sum)
        rightSum = find_tilt_helper(root.right, sum)
        currTilt = abs(leftSum - rightSum)
        return root.val + currTilt

    totalTilt = 0
    totalTilt =  find_tilt_helper(root,totalTilt)
    return totalTilt

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
# print(find_tilt(root))