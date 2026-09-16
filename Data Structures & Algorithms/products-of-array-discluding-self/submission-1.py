class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left, right = [1]*n,[1]*n
        
        for i in range(n):
            if i-1>=0:
                left[i] = nums[i-1]*left[i-1]
        for i in range(n-1,-1,-1):
            if i+1<len(nums):
                right[i] = nums[i+1]*right[i+1]
        # print(left, right)     
        ans = [1]*n
        for i in range(len(nums)):
            ans[i] = left[i]*right[i]
        return ans