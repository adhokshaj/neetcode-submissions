class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i,j = 0,0
        ans = 0
        for j in range(n):
            if prices[j]<prices[i]:
                i = j
            ans = max(ans, prices[j]-prices[i])
        return ans
            