from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i):
            if i==n: return 1
            if s[i]=='0': return 0
            ways = 0
            for j in range(i,n):
                if int(s[i:j+1]) in range(1,27):
                    ways += dfs(j+1)
            return ways
        return dfs(0)