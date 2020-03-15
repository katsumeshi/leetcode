class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(grid[0])
        flat = sum(grid, [])
        l = len(flat)
        m = k % l
        flat = flat[l-m:] + flat[:l-m]
        return [flat[i:i + n] for i in xrange(0, l, n)]
