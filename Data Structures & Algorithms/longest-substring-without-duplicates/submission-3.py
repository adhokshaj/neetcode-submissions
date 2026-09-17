class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l,r,n = 0, 0 , len(s)
        ans = 0
        while r<n:
            # shrink the window till it is invalid
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            ans = max(ans, r-l+1)
            r += 1
        return ans

        