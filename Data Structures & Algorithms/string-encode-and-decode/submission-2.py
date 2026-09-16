class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str  = ""
        for word in strs:
            encoded_str += str(len(word)) + "*" + word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # print(s)
        l,r, n  = 0,0, len(s)
        ans = []
        while r<n:
            len_str = ""
            while s[r]!='*':
                len_str += s[r]
                r += 1
            # print(len_str)
            width = int(s[l:r])
            ans.append(s[r+1:r+width+1])
            r = r+width+1
            l = r
        return ans

