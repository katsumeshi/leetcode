class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def canRotton(x, y):
            if 0 <= x < lx and 0 <= y < ly and grid[y][x] == 1:
                return True
            return False
        
        arr = []
        lx = len(grid[0])
        ly = len(grid)
        move = [(1, 0),(-1, 0),(0,1),(0,-1)]
        fresh = False
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 2:
                    arr.append((x, y))
                if grid[y][x] == 1:
                    fresh = True
        
        if len(arr) == 0:
            if fresh ==True:
                return -1
            else:
                return 0
        
        count = 0
        while len(arr) > 0:
            tmp = []
            while len(arr) > 0:
                tmp.append(heapq.heappop(arr))
            for (x, y) in tmp:
                for (mx, my) in move:
                    nx, ny = x+mx, y+my
                    if canRotton(nx, ny):
                        heapq.heappush(arr, (nx, ny))
                        grid[ny][nx]=2
            count+=1
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    return -1
                
        return count-1
