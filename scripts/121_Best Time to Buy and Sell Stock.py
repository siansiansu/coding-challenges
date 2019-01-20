class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        low = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            maxprofit = max(maxprofit, prices[i] - low)
        return maxprofit
