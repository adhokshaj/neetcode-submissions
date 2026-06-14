class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res = res + str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:

        ans = []

        l, r  = 0, 0
        while r<len(s):
            # print(s)
            # print(l,r)
            # print(ans)
            l1, r1 = l, l
            while s[r1] != '#':
                r1 += 1
            # print(l1,r1)
            str_len = int(s[l1:r1])
            l = r1+1
            r = r1+str_len+1
            if str_len==0:
                ans.append("")
                continue
            if l<len(s) and r<=len(s):
                ans.append(s[l:r])
            l = r1+str_len+1
        return ans

