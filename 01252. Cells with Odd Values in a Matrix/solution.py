class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        arr = []
        for i in range(n):
            arr.append([0] * m)
        
        for i, j in indices:
            for c in range(m):
                arr[i][c] += 1
            for r in range(n):
                arr[r][j] += 1
        count = 0
        for rows in arr:
            for v in rows:
                if v % 2 != 0:
                    count += 1
        return count
