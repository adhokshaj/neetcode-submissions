from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dfs(i, rem):
            if rem==0:
                return 0
            if i==n:
                return float('inf')
            ans = float('inf')
            if rem-coins[i]>=0:
                ans = min(ans, 1+dfs(i, rem-coins[i]))
            ans = min(ans,dfs(i+1,rem))
            return ans
        ans = dfs(0, amount)
        return ans if ans!=float('inf') else -1

        