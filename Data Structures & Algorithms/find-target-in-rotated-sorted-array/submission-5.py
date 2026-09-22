class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            # print(mid,l,r)
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[n-1]: # mid in right sorted array
                if target>nums[mid] and target<=nums[n-1]:
                    l = mid+1
                else:
                    r = mid-1
            else:                     # mid in left sorted array
                if target<nums[mid] and target>=nums[0]: 
                    r = mid-1
                else:
                    l = mid+1
        return -1

        