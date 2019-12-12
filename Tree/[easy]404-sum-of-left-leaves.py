# ========================= Problem Description   ============================================
#
#Find the sum of all left leaves in a given binary tree.
#
#Example:
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
#There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


# ------------------------------------------------------------------------
# Solution
# use L->V->R inorder tree traversal
# during the left TreeNode iteration, calculate the iterated node number
# if number > 1 (not the root of subtree), sum it to the sum_of_lleaf
# ------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        sum_of_lleaf = 0
        
        if not root:
            return 0
        
        current = root
        stack = []
        
        while True:
            if current:
                height = 0
                while current:
                    height +=1 
                    stack.append(current)
                    current = current.left
                if height > 1 and stack[-1].right is None:
                    sum_of_lleaf += stack[-1].val
            elif stack:
                current = stack.pop()
                current = current.right
            else:
                break
                    
        return sum_of_lleaf