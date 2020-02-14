class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = len(chars)-1
        count = 1
        while i >= 0:
            if chars[i-1] != chars[i] or i == 0:
                if count > 1:
                    chars.insert(i+1, str(count)) 
                if count > 9:
                    del chars[i+1]
                    for v in list(str(count))[::-1]:
                        chars.insert(i+1, v)
                count = 0
            else:
                del chars[i]
            count+=1
            i-=1
        return len(chars)
