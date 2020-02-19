class Solution(object):
    def convertToBase7(self, num, ret="", minus=None):
        """
        :type num: int
        :rtype: str
        """
        if minus is None:
            minus = "-" if num < 0 else ""
            num = abs(num)
        if 7 > num:
            return minus+str(num)+ret
        return self.convertToBase7(num/7, str(num%7)+ret, minus)
