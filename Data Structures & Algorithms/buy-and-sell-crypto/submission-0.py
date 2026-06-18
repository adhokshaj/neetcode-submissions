class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l,r = 0, 1
        maxx = 0
        while r<n:
            maxx = max(maxx, prices[r]-prices[l])
            if prices[r]<prices[l]:
                l = r
            r += 1
        return maxx
        