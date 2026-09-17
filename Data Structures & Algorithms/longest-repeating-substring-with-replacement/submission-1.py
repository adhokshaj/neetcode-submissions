class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        l, r, n = 0, 0, len(s)
        ans = 0
        max_f = 0
        for r in range(n):
            freq_map[s[r]] += 1
            max_f = max(max_f, freq_map[s[r]])
            while (r-l+1)-max_f>k:
                freq_map[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans


            
        