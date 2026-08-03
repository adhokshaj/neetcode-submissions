class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {i:j for j,i in enumerate(nums)}
        # print(index_map)
        for i,num in enumerate(nums):
            if target-num in index_map.keys() and index_map[target-num]!=i:
                return [i, index_map[target-num]]
        return []