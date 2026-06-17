class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {num:i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if  (target-num in index_map.keys() and 
                i != index_map[target-num]):
                return [i, index_map[target-num]]
        return []
        


            
        