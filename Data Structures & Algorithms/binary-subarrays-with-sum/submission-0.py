class Solution:
    def atMost(self,nums, k):
        l,n = 0, len(nums)
        res, window = 0, 0
        for r in range(n):
            window += nums[r]
            while l<=r and window > k:
                window -= nums[l]
                l += 1
            res += r-l+1
        return res
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMost(nums, goal)-self.atMost(nums, goal-1)
        