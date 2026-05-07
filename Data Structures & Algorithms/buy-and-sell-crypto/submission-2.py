class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                netProfit = prices[j] - prices[i]
                if netProfit > 0:
                    result = max(result, netProfit)                    
        return result