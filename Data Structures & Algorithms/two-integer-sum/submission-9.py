class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {num:i for i,num in enumerate(nums)}
        for i,num in enumerate(nums):
            if target-num in num_map and num_map[target-num]!=i:
                return [i, num_map[target-num]] 
        return []