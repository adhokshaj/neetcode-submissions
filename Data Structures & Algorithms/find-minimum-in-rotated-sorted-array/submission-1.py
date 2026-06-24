class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        ans = nums[0]

        while l<=r:
            m = l + (r-l)//2
            # print(nums[m])
            if nums[m] < nums[0]: # this means right part is sorted
                r = m-1
            else:
                l = m+1
            ans = min(ans, nums[m])
        return ans