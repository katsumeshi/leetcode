class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for ss in s:
            m[ss] = 1 if ss not in m else m[ss] + 1
                
        for i in range(len(s)):
            if m[s[i]] == 1:
                return i
        return -1
