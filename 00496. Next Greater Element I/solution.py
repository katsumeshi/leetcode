class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)-1):
                if nums1[i] == nums2[j]:
                    for k in range(j+1, len(nums2)):
                        if nums1[i] < nums2[k]:
                            nums1[i] = nums2[k]
                            found = True
                            break
                    if found:
                        break
            if not found:
                nums1[i] = -1
        return nums1
