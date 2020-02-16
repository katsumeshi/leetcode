# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, "")
        
    def dfs(self, root, s):
        if root is None:
            return 0
        s += str(root.val)
        if root is not None and root.left is None and root.right is None:
            return int(s,2)
        return self.dfs(root.left, s) + self.dfs(root.right, s)
