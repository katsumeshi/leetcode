class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kind = len(set(candies))
        half = len(candies) / 2
        return kind if half > kind else half
