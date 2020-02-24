class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S, l, r = list(S), 0, len(S)-1
        while l < r:
            if re.match('[a-zA-Z]', S[l]) == None:
                l+=1
            elif re.match('[a-zA-Z]', S[r]) == None:
                r-=1
            else:
                S[l], S[r] = S[r], S[l]
                l, r = l+1, r-1
        return "".join(S)
