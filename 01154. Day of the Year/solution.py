class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        ymd = date.split("-")
        ymd = map(lambda v: int(v), ymd)
        m = ymd[1]-1
        ans = ymd[2]
        for i in range(m):
            ans+=days[i]
        if m >= 2 and ymd[0] % 4 == 0 and ymd[0] % 100 != 0:
            ans += 1
        return ans
