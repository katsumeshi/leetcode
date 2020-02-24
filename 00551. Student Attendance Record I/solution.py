class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for r in s:
            if 'A' in r:
                a += 1    
            if 'L' in r:
                l += 1
            else:
                l = 0
            if a > 1 or l > 2:
                return False
        return True
