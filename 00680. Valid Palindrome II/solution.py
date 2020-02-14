class Solution(object):
    def validPalindrome(self, s, count=0):
        """
        :type s: str
        :rtype: bool
        """
        a = s
        b = s[::1]
        h = len(s)//2
        i = 0
        if count == 2:
            return False
        while i < h:
            if a[i] != b[len(s)-1-i]:
                s = s[i:len(s)-i]
                return self.validPalindrome(s[:len(s)-1], count+1) or self.validPalindrome(s[1:], count+1)
            i+=1
        return True
