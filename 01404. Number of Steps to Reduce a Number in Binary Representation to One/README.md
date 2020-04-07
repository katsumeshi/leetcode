class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = int(s, 2)
        count = 0
        while b > 1:
            if b % 2 == 0:
                b /= 2
            else:
                b += 1
            count += 1
        return count
