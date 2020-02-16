class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        for i in range(len(bits)-1):
            if bits[i] == 1:
                bits[i] = -1
                bits[i+1] = -1
        if bits[len(bits)-1] == -1:
            return False
        return True
