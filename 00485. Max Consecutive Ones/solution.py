class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        count=0
        while len(nums) > 0:
            if nums.pop() == 1:
                count+=1
            else:
                ret = max(count, ret)
                count = 0
        return max(count, ret)
