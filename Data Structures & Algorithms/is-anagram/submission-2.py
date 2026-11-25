class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_arr = [0]*26
        t_arr = [0]*26

        for c in s:
            ind = ord(c)-ord('a')
            s_arr[ind] += 1
        
        for c in t:
            ind = ord(c)-ord('a')
            t_arr[ind] += 1

        return s_arr==t_arr
        