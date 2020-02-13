class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.execute(S) == self.execute(T)
        
    def execute(self, A):
        i = 0
        while i < len(A):
            if A[i] == "#":
                A = A[:max(i-1,0)] + A[min(i+1,len(A)):]
                i = 0
            else:
                i += 1
        return A
