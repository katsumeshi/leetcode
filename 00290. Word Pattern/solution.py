class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def toDigitPattern(arr):
            d, c  = {}, []
            for p in arr:
                if p in d:
                    c.append(d[p])
                else:
                    d[p] = len(d)
                    c.append(d[p])
            return c
        return toDigitPattern(pattern) == toDigitPattern(str.split(" "))
