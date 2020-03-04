class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        result = ""
        while len(s) > i:
            if i+2 < len(s) and s[i+2] == "#":
                n = s[i:i+2]
                i+= 3
            else:
                n = s[i]
                i+=1
            result += chr(int(n)+96)
        return result
