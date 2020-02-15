class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for value in strs:
            sumChars = []
            for char in value:
                sumChars.append(str(ord(char)))
            sumChars = sorted(sumChars)
            key = "".join(sumChars)
            if key not in d:
                d[key] = [value]
            else:
                d[key].append(value)
        print d
        ret = [] 
        for key in d:
            group = []
            for value in d[key]:
                group.append(value)
            ret.append(group)
        return ret
