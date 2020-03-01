class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, c = 0, 0
        while len(A) > c:
            if A[i] % 2 == 1:
                A.append(A.pop(i))
                i-=1
            i+=1
            c+=1
        return A
