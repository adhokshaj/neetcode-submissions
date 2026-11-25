class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_to_list = defaultdict(list)
        for word in strs:
            hash = [0]*26
            for c in word:
                ind = ord(c)-ord('a')
                hash[ind] += 1
            hash_to_list[tuple(hash)].append(word)
        return list(hash_to_list.values())
        