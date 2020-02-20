class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        def index(value):
            try:
                return value.index(C)
            except ValueError:
                return len(S)
        
        ret=[]
        for i in range(len(S)):
            ret.append(min(index(S[0:i+1][::-1]), index(S[i:])))
        return ret
        
