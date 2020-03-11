# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root, ans = True):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is not None:
            if root.left is not None:
                ans = self.isUnivalTree(root.left, root.val == root.left.val and ans)
            if root.right is not None:
                ans = self.isUnivalTree(root.right, root.val == root.right.val and ans)
        return ans
