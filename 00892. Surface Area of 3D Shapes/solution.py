class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cubeCount, overlap = 0, 0
        for i in range(len(grid)):
            last = grid[i][len(grid[i])-1]
            side, behind, stuck = 0, 0, max(0, last-1)
            cubeCount += last
            for j in range(max(0, len(grid[i])-1)):
                stuck += max(grid[i][j]-1, 0)
                side += min(grid[i][j], grid[i][j+1])
                behind += min(grid[j][i], grid[j+1][i]) 
                cubeCount += grid[i][j]
            overlap += side + behind + stuck
        return cubeCount * 6 - overlap * 2
