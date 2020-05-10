class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        a = [0] * N
        for t in trust:
            a[t[1]-1]+=1
            a[t[0]-1]-=1
        ans = -1
        for i in range(len(a)):
            if a[i] == N-1:
                ans = i+1
        return ans
