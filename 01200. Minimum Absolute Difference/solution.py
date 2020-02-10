class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        minDiff = sys.maxint
        
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            minDiff = min(diff, minDiff)
        
        ret = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == minDiff:
                ret.append([arr[i], arr[i+1]])
        return ret
