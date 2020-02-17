class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        s = [str(i) for i in A] 
        value = int("".join(s)) 
        return list(str(value + K))
