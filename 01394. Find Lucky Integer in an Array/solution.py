class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr = collections.Counter(arr).most_common()
        for v in arr:
            if v[0] == v[1]:
                return v[0]
        return -1
