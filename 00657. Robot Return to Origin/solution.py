class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {"L": -1, "R": 1, "U": 100, "D": -100}
        result = 0
        for m in moves:
            result += d[m]
        return result == 0
