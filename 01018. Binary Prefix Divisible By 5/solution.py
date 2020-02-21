class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        total = 0
        length = len(A)
        ret = [False] * length
        val = 2**(length-1)
        for i in range(length):
            total += val * A[i]
            if total % 5 == 0:
                ret[i] = True
            val /= 2
        return ret
