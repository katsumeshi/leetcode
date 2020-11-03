class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = s[0]
        s = s[1:]
        count, ans = 1, 0
        for char in s:
            if prev == char:
                count += 1
            else:
                ans = max(count, ans)
                count = 1
            prev = char
        return max(count, ans)
