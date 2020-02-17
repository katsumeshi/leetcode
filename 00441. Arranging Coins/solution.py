class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        s = 0
        while s + i <= n:
            s += i
            i = i + 1
        return i - 1
