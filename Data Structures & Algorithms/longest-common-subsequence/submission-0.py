from functools import cache
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        @cache
        def dfs(i,j):
            if i==n or j==m:
                return 0
            
            #take
            take = 0
            if s[i]==t[j]:
                take = 1 + dfs(i+1,j+1)

            #dont_take
            dont_take = max(dfs(i+1,j), dfs(i,j+1), dfs(i+1, j+1))

            return max(take, dont_take)
        
        return dfs(0,0)
        