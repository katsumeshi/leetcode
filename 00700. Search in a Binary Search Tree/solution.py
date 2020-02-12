# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        q = [root]
        while len(q) > 0:
            n = heapq.heappop(q)
            
            if n is None:
                continue
                
            if n.val == val:
                return n

            heapq.heappush(q, n.left)
            heapq.heappush(q, n.right)
            
        return None
