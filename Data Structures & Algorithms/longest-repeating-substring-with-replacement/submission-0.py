
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        n = len(s)
        l,n,maxf,res = 0, len(s), 0, 0
        # Following add, check and find max pattern
        for r in range(n):
            window[s[r]] += 1
            maxf = max(maxf, window[s[r]])
            # shrink the window till its valid
            while (r-l+1)-maxf>k:
                window[s[l]] -= 1
                l += 1
            #update res
            res = max(res, r-l+1)
        return res

        