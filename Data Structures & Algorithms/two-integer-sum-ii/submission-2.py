class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def two_pointer_solution():
            l, r = 0, len(nums)-1
            while l<r:
                if nums[l]+nums[r]>target:
                    r -= 1
                elif nums[l]+nums[r]<target:
                    l += 1
                else:
                    return [l+1,r+1]
        
        def binary_search_solution():
            def binarySearch(l,r,arr, t):
                while l<=r:
                    m = (l+r)//2
                    # print(l, r, m)
                    if arr[m]==t:
                        return m
                    elif arr[m]<t:
                        l = m+1
                    else:
                        r = m-1
                return -1

            for i, num in enumerate(nums):
                pos = binarySearch(0, len(nums)-1, nums, target-num)
                print(pos)
                if  pos!= -1:
                    return [i+1, pos+1]
            
            return []
        
        return binary_search_solution()