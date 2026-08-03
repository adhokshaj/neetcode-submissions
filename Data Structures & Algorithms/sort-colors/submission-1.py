class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i,j,k = 0, n-1, 0

        def swap(a,b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

        while k<=j:
            if nums[k] ==0:
                swap(i,k)
                i += 1
            elif nums[k]==2:
                swap(j,k)
                j -= 1
                k -= 1
            k += 1
            # print(nums)
        

        