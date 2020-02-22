class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i in range(len(s)):
            ret += (ord(s[len(s)-i-1]) - 64) * (26 ** i)
        return ret
