class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        f1, f2 = [0]*26, [0]*26
        for c in s1:
            f1[ord(c)-ord('a')] += 1
        l,r,n = 0,0,len(s2)
        match = 0
        while r<len(s1):
            c = s2[r]
            f2[ord(c)-ord('a')] += 1
            r += 1
        # print(f1, f2)
        for i in range(26):
            if f1[i]==f2[i]:
                match += 1

        while r<=len(s2):
            # print(s2[l:r], match, f1, f2, r)
            if match==26:
                return True
            
            
            if r<len(s2):
                # move r
                c = s2[r]
                ind = ord(c)-ord('a')
                f2[ind] += 1
                if f1[ind] == f2[ind]-1:
                    match -= 1
                elif f1[ind] == f2[ind]:
                    match += 1
            
                #move l
                c = s2[l]
                ind = ord(c)-ord('a')
                f2[ind] -= 1
                if f1[ind] == f2[ind]+1:
                    match -= 1
                elif f1[ind] == f2[ind]:
                    match += 1
            
            r += 1
            l += 1
        
        return False
            
            
        