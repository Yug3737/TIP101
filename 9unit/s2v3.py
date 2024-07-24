
# level order traversal in dictionary
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
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
    q = val_q = deque()
    left_corner = right_corner = None
    if root:
        q.append(root)
        val_q.append(root.val)
        left_corner = val_q[0]
        right_corner = val_q[-1]
        if left_corner == right_corner:
            print(left_corner)
        
        while q:
            qlen = len(q)
            
            for _ in range(qlen):
                curr = q.popleft()
                print(type(curr))
                if curr.left:
                    q.append(curr.left)
                    val_q.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    val_q.append(curr.right.val)
            print(val_q[0], val_q[-1])

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print_corner_nodes(root)

        