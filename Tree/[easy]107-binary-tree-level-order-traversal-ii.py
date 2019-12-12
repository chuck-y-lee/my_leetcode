#Problem Description
#Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
#(ie, from left to right, level by level from leaf to root).
#
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  0
#    /  \
#   15   7
#return its bottom-up level order traversal as:
#[
#  [15,7],
#  [9,20],
#  [3]
#]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# --------------------------------------------------------------------------------------------
# Solution:
# [BFS]
# Use 2 stacks: stack0, stack1 to collect the nodes of the same levels
# stack0 is initialized with root node, then put its child nodes to stack1
# Then swap stack0 and stack1 to iterate nodes of next level until stack0 have no more nodes
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """        
        if not root:
            return []
        
        level_bot_node_arr = deque()
        stack0 = [root]
        stack1 = []   
        while stack0:
        
            level_arr = []
        
            for node in stack0:
                level_arr.append(node.val)
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)


            level_bot_node_arr.appendleft(level_arr)
            del(stack0[:])
            stack0, stack1 = stack1, stack0

        return list(level_bot_node_arr)


#from common import *
#
#root = stringToTreeNode('[3,9,20,null,null,15,7]')
#sol = Solution()
#print(sol.levelOrderBottom(root))