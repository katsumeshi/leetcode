class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        if len(s) <= 1:
            return num
        num = 0
        for c in s:
            num += int(c)
        return self.addDigits(num)
