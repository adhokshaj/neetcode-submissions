class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        patt_group = defaultdict(list)
        for word in strs:
            patt = [0]*26
            for c in word:
                patt[ord(c)-ord('a')] += 1
            key = tuple(patt)
            patt_group[key].append(word)
        # print(patt_group.values())
        return list(patt_group.values())
        