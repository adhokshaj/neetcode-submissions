class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #   rule of sliding window: find the required information in the current
        #   window(which should be always valid, if not shrink the window from left
        #   as we have already tested the window with the previous left). 

        n = len(s)
        l, r = 0, 0
        curr = set()
        maxx = 0
        while r<n:
            #   shrink the window till its valid
            while curr and (s[r] in curr) and l<r:
                curr.remove(s[l])
                l += 1
            
            # Now the window is valid, find the required information
            maxx = max(maxx, r-l+1)

            curr.add(s[r])
            r += 1
        return maxx





        