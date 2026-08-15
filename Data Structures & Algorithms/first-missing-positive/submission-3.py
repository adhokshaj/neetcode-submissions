class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i]<0:
                nums[i] = 0
        for i,num in enumerate(nums):
            if abs(num)>0 and abs(num)-1>=0 and abs(num)-1<n and nums[abs(num)-1]>=0:
                if nums[abs(num)-1]==0:
                    nums[abs(num)-1] = -(n+1)
                else:
                    nums[abs(num)-1] *= -1
        # print(nums)
        i = 0
        while i<n:
            if nums[i]>=0:
                return i+1
            i += 1
        return i + 1


        