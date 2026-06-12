class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for str in strs:
            key = tuple(sorted(dict(Counter(str)).items()))

            # 1. Get the existing list or a temporary empty list
            current_list = anagram_map.get(key, [])

            # 2. Append the new string
            current_list.append(str)

            # 3. Write it back into the dictionary so it is saved
            anagram_map[key] = current_list

            # print(anagram_map)
        res = []
        for entry in anagram_map.values():
            res.append(entry)
        return res


        
        