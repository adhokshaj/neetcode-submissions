class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        ans = float('inf')
        while l<=r:
            mid = (l+r)//2
            if nums[n-1]>=nums[mid]: # mid in right sorted array
                r = mid-1
                ans = min(ans, nums[mid])
            else:
                l = mid + 1
        return ans
