class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        
        n = []
        for i in range(len(nums)):
            n += nums[i]
        
        arr = []
        for i in range(r):
            arr.append(n[c*i:c*(i+1)])
        return arr
