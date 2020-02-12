class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        m = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    a = (points[i][0] - points[k][0]) *  (points[j][1] - points[k][1]) 
                    b = (points[j][0] - points[k][0]) *  (points[i][1] - points[k][1])
                    m = max(m, abs(a - b) /2.0)
        return m
