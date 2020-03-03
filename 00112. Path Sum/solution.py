# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(root, sum):
            
            reuslt = False
            if root.left is not None and reuslt == False:
                reuslt = dfs(root.left, sum-root.left.val)
            if root.right is not None and reuslt == False:
                reuslt = dfs(root.right, sum-root.right.val)
            if root.left is None and root.right is None:
                reuslt = sum == 0
            return reuslt
            
        if root is None:
            return False
        
        return dfs(root, sum-root.val)
