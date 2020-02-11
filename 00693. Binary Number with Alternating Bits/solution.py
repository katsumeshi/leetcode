class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits = bin(n)[2:]
        prev = ""
        for bit in bits:
            if bit == prev:
                return False
            prev = bit
        return True
