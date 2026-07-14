from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        # print(chr(65))
        n = len(s)
        # letter_map = {}
        # for i in range(65,91):
        #     letter_map[chr(i)] = (i-65)+1
        # print(letter_map)
        @cache
        def dfs(i):
            # print(i)
            if i==n: return 1
            if s[i]=='0': return 0
            ways = 0
            for j in range(i,n):
                # print(s[i:j+1])
                if int(s[i:j+1]) in range(1,27):
                    ways += dfs(j+1)
            return ways
        return dfs(0)