from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i,j):
            if (i<0 or i==m or j<0 or j==n): return 0
            if i==m-1 and j==n-1: return 1

            #right
            right = dfs(i+1,j)

            #bottom
            bottom = dfs(i,j+1)

            return right+bottom
        return dfs(0,0)

        