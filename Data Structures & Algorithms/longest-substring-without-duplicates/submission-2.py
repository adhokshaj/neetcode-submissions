class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            sliding-window pattern
            - Longest
                - Use a for loop to move the r pointer
                - While invalid move the l pointer at every r
                - Now its valid so update the max
            - Shortest
                - Use a for loop to move the r pointer
                - While valid move the l pointer at every r
                - Inside valid loop update the min
        '''

        l,n = 0, len(s)
        window = set()
        ans = 0
        # Following check, add and update max pattern
        for r in range(n):
            # check if window will be valid after adding s[r], current window [l,r-1]
            #    - shrink window until its valid
            while s[r] in window:
                window.remove(s[l])
                l += 1
            # Now window is valid if s[r] is added
            window.add(s[r])
            ans = max(ans, r-l+1)
        return ans

            



        