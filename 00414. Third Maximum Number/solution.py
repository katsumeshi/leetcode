class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        de = collections.deque([-sys.maxint - 1] * 3)
        for n in nums:
            if de[2] < n:
                de.popleft() 
                de.append(n) 
            elif de[1] < n:
                de.popleft()
                de.insert(1, n) 
            elif de[0] < n:
                de.popleft() 
                de.appendleft(n) 
        if len(nums) <= 2:
            return de[2]
        return de[0]
