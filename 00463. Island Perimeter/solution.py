class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def getStart():
            for i in range(len(grid)):
                 for j in range(len(grid[i])):
                        if grid[i][j] == 1:
                            return (i, j)
        
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pos = {}
        def dfs(x, y):
            for m in move:
                nX, nY = x+m[0], y+m[1]
                if (nX,nY,m[0],m[1]) in pos:
                    break
                if 0 <= nX < len(grid) and 0 <= nY < len(grid[0]):
                    if grid[nX][nY] == 1:
                        grid[nX][nY] = -1
                        dfs(nX, nY)
                    elif grid[nX][nY] == 0:
                        pos[(nX,nY,m[0],m[1])] = 1
                else:
                    pos[(nX,nY,m[0],m[1])] = 1
        (i, j) = getStart()
        dfs(i, j)
        return len(pos)
                
