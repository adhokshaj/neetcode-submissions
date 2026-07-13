from functools import cache
class Solution:
    def rob(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def dfs(i, m):
            if i>=m: return 0
            return max(cost[i] + dfs(i+2,m), dfs(i+1,m))
        return max(dfs(0,n-1), dfs(1,n),cost[0])
        