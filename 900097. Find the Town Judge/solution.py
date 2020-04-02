class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust) == 0:
            return N
        
        ppl = {}
        for t in trust:
            ppl[t[0]] = ppl[t[0]]-1 if t[0] in ppl else -1
            ppl[t[1]] = ppl[t[1]]+1 if t[1] in ppl else 1
        
        a, b = collections.Counter(ppl).most_common()[0]
        if N-1 == b:
            return a
        return -1
                
