class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy, zx, yz = 0, 0, 0
        tmpYZ = [0] * len(grid[0])
        for i in xrange(len(grid)):
            tmpZX = 0
            for j in xrange(len(grid[i])):
                if grid[i][j] >= 1:
                    xy += 1
                tmpZX = max(tmpZX, grid[i][j])
                tmpYZ[j] = max(tmpYZ[j], grid[i][j])
            zx += tmpZX
        yz = sum(tmpYZ)
        return xy+zx+yz
