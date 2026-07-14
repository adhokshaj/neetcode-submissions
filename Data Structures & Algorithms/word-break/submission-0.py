from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        @cache
        def dfs(i):
            if i==n: return True
            ans = False
            for j in range(i,n):
                if s[i:j+1] in wordSet:
                    ans = ans or dfs(j+1)
            return ans
        return dfs(0)
        