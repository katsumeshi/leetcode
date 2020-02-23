class Solution(object):
    def numEquivDominoPairs(self, d):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        ret = 0
        dic = {}
        for i in range(len(d)):
            x = d[i][0] if d[i][0] < d[i][1] else d[i][1]
            y = d[i][0] if d[i][0] > d[i][1] else d[i][1]
            dic[(x, y)] = 0 if (x, y) not in dic else dic[(x, y)] + 1
            
        for key in dic:
            v = dic[key]
            while v > 0:
                ret += v
                v -= 1
        return ret
