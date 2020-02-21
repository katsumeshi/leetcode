class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = -1
        while prev != len(s):
            prev = len(s)
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return len(s) == 0
