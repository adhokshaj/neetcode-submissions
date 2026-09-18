class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # condition: have==want, until the condition is true shrink it

        win, f = defaultdict(int), defaultdict(int)
        for c in t:
            f[c] += 1
        
        have, want = 0, len(f)
        
        l,r,n = 0, 0, len(s)
        ans, min_len = "", float('inf')

        while r<n:
            
            #include r
            ind = s[r]
            win[ind] += 1

            if f[ind]!=0 and win[ind]==f[ind]:
                have += 1
            
            # print(win, have, s[l:r+1])
            # shrink window
            while have==want:
                if(r-l+1)<min_len:
                    min_len = r-l+1
                    ans = s[l:r+1]
                ind = s[l]
                win[ind] -= 1
                l += 1
                if f[ind]!=0 and win[ind] + 1 == f[ind]:
                    have -= 1
            r += 1
        return ans
                
            
            
        