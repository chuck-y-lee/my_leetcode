# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        paths = []
        
        def find_paths(root,path):            
            path.append(str(root.val))
            if root.left is None and root.right is None:
                paths.append('->'.join(path))
            if root.left:
                find_paths(root.left, path)
            if root.right:
                find_paths(root.right, path)
            path.pop()
        
        find_paths(root,[])
        return paths

#from common import *
#sol=Solution()
#
#testcases = ['[1,2,3,4,5,null,7,null,null,null,9,10,null,null,null]']
#for case in testcases:
#    root = stringToTreeNode(case)
#    print(sol.binaryTreePaths(root))