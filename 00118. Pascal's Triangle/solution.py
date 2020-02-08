class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        for i in range(numRows):
            l.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    l[i].append(1)
                else:
                    l[i].append(l[i-1][j-1]+l[i-1][j])
        return l
