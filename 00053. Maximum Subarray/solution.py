class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = maxSum = nums[0]
        for i in range(1,len(nums)):
            currentSum =  max(currentSum+nums[i], nums[i]) 
            maxSum = max(maxSum, currentSum)
        return maxSum
