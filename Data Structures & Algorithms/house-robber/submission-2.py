from functools import cache

class Solution:
    def rob(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def dfs(i):
            if i>=n: return 0
            return max(cost[i] + dfs(i+2), dfs(i+1))
        return max(dfs(0), dfs(1))
        

        