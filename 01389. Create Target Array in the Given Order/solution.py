class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(index)):
            arr.insert(index[i], nums[i])
        return arr
