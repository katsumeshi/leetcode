# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # if len(p) == 0 and len(q) == 0:
        #     return False
        # if not p and not q:
        #     return True
        
        p = deque([p])
        q = deque([q])
        while p and q:
            a = p.popleft()
            b = q.popleft()
            if  (a and not b) or (not a and b) or ((a and b) and (a.val != b.val or (a.left and not b.left) or (a.right and not b.right) or (not a.left and b.left) or (not a.right and b.right))):
                return False
            
            if a:
                if a.left:
                    p.append(a.left)
                if a.right:
                    p.append(a.right)
            if b:
                if b.left:
                    q.append(b.left)
                if b.right:
                    q.append(b.right)
            
        return len(p) == len(q)
