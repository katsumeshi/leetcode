class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        l = len(s)
        pos = 0
        while len(shift):
            a, b = shift.pop(0)
            pos += -b if a == 0 else b
        pos = pos%l
        return s[l-pos:] + s[:l-pos] if pos > 0 else s[-pos:] + s[:-pos]
