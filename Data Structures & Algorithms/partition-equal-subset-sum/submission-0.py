from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        @cache
        def dfs(i, cur):
            if i==n:
                return cur==total-cur
            if cur==total-cur:
                return True
            
            
            #take
            take = dfs(i+1, cur+nums[i])

            #dont_take
            dont_take = dfs(i+1, cur)

            return take or dont_take
        
        return dfs(0,0)
            