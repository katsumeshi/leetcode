class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ret = -sys.maxint - 1
        prev = None
        for i in range(len(nums)-(k-1)):
            if prev is None:
                prev = sum(nums[i:i+k])
            else:
                prev = prev - nums[i-1] + nums[i+k-1]
            ret = max(ret, prev/(k*1.0))
        return ret
