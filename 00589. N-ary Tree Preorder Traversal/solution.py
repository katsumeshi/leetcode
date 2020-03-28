"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        arr = []
        def dfs(root):
            if not root:
                return
            arr.append(root.val)
            for r in root.children:
                dfs(r)
        dfs(root)
        return arr
