class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = {}
        for v in nums:
            if v not in a:
                a[v] = 1
            else:
                return True
            
        return False
