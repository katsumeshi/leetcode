class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bits = bin(N)[2:]
        result = 0
        while len(bits) > 0:
            try:
                index = bits[1:].index("1")+1
                result = max(index, result)
                bits = bits[index:]
                print bits
            except ValueError:
                return result
        return result
