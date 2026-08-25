class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, n = 0, len(nums)
        curSum, atLeast = 0, float('inf')
        for r in range(n):
            curSum += nums[r]
            # shrink until its valid
            while curSum>=target:
                atLeast = min(r-l+1, atLeast)
                curSum -= nums[l]
                l += 1
        if atLeast==float('inf'):
            return 0
        return atLeast

            
        