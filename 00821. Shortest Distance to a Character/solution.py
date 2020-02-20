class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ret=[]
        for i in len(S):
            ret.append(min(S[i:].indexofOf(C), S[:i].indexOf(C)))
            return ret
