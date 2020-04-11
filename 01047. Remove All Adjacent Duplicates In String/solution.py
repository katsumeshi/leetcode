class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        remove = False
        while i < len(S)-1:
            if S[i] == S[i+1]:
                S = S[:i] + S[i+2:]
                remove = True
                continue
            i+=1
        return self.removeDuplicates(S) if remove else S
