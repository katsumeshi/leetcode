class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = list(reversed(sorted(nums)))
        for i in range(len(arr)):
            if sum(arr[:i]) > sum(arr[i:]):
                return arr[:i]
        return arr
