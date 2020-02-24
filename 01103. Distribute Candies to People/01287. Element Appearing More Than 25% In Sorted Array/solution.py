class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return collections.Counter(arr).most_common(1)[0][0]
