class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        ones = int("1" * len(bin(N)[2:]), 2)
        return int(bin(~N & ones)[2:], 2)
