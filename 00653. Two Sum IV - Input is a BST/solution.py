# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = [root]
        values=[]
        while len(queue) > 0:
            node = heapq.heappop(queue)
            if node is None:
                continue
            values.append(node.val)
            
            heapq.heappush(queue, node.left)
            heapq.heappush(queue, node.right)
            
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                if k == values[i] + values[j]:
                    return True
                
        return False
