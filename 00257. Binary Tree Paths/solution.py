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
        def dfs(root, arr, s):
            if root.left is not None:
                dfs(root.left, arr, s + str(root.left.val) + "->")
            if root.right is not None:
                dfs(root.right, arr, s + str(root.right.val) + "->")
                
            if root.left is None and root.right is None:
                arr.append(s[:len(s)-2])
            return arr
        
        if root is None:
            return []
        
        return dfs(root, [], str(root.val) + "->")
