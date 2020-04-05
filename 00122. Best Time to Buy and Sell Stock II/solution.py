class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        buy = prices[0]
        sell = total = 0
        i = 1
        while len(prices) > i:
            if prices[i-1] > prices[i]:
                total += sell
                sell = 0
                buy = prices[i]
            sell = max(prices[i]-buy, sell)
            i+=1
        return max(sell, total+sell)
