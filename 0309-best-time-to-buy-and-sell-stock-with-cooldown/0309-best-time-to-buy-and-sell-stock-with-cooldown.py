class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0, dp1, dp2 = 0, -prices[0], 0
        for p in prices:
            dp0, dp1, dp2 = max(dp0, dp2), max(dp1, dp0 - p), dp1 + p
        return max(dp0, dp2)