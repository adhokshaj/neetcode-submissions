class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finger_print_map = defaultdict(list)
        for str in strs:
            finger_print = [0]*26
            for s in str:
                index = (ord(s)-ord('a'))
                # print(index)
                finger_print[index] += 1
            finger_print_map[tuple(finger_print)].append(str)
        # print(finger_print_map)
        return list(finger_print_map.values())

        