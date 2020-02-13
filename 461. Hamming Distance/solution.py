class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return len(re.sub('0', '', str(bin(x^y)[2:]))) 
