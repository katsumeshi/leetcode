class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        d = {0:0, 1:0}
        for p in position:
            d[p%2]+=1
        
        return min(d[0], d[1])
