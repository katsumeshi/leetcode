# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.dfs(root, 0, [])

    def dfs(self, root, depth, arr):
        if root is not None:
            if len(arr)-1 < depth:
                arr.append([root.val])
            else:
                arr[depth].append(root.val)
            
            if root.left is not None:
                self.dfs(root.left, depth+1, arr)
            if root.right is not None:
                self.dfs(root.right, depth+1, arr)
        
        return arr[::-1]
            
