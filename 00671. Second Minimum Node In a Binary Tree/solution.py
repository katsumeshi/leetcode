# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max = sys.maxint
        d = [max-1, max]
        def dfs(root):
            if not root:
                return
            
            if root.val < d[0] < d[1]:
                d[0] = root.val
            elif d[0] < root.val < d[1]:
                d[1] = root.val
                
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return -1 if d[1] == max else d[1]
