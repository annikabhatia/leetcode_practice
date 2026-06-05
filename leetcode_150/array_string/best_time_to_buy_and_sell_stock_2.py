# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                profit+=(prices[i+1] - prices[i])
            
                
        return profit

# Example usage:
solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = solution.maxProfit(prices)
print(result)  # Output: 7 (buy at 1, sell at 5, buy at 3, sell at 6)