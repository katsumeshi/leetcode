class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def isValid(x, y, c):
            if 0 <= x < len(image) and 0 <= y < len(image[x]) and c == image[x][y]:
                return True
            return False
        
        def dfs(x, y, c):
            image[x][y] = newColor
            for d in dir:
                nx = x+d[0]
                ny = y+d[1]
                if isValid(nx, ny, c):
                    dfs(nx, ny, c)
         
        c = image[sr][sc]
        if c == newColor:
            return image
        
        dfs(sr, sc, c)
        return image
