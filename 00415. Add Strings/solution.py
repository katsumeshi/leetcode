class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l = max(len(num1), len(num2))
        ret=""
        carry = 0
        for i in range(l):
            total = carry
            if len(num1) > i:
                total += ord(num1[len(num1)-i-1]) - ord('0')
            if len(num2) > i:
                total += ord(num2[len(num2)-i-1]) - ord('0')
            ret = str(total%10) + ret
            carry = 1 if total > 9 else 0
        if carry > 0:
            ret = "1" + ret
        return ret
