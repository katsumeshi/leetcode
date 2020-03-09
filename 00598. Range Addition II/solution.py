class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        maxm, maxn = m, n
        for o in ops:
            maxm, maxn = min(o[0], maxm), min(o[1], maxn)
        return maxm*maxn
