class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n):
            if "0" not in str(n - i) and "0" not in str(i) :
                return [i, n - i]
