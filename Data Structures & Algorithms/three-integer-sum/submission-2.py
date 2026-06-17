class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        i, j, k, n = 0, 1, 2, len(nums)

        def two_sum(p,q,t):
            ans = []
            while p<q:
                if nums[p]+nums[q]==t:
                    ans.append([nums[p], nums[q]])
                    while p<q and nums[p+1]==nums[p] and nums[q-1]==nums[q]:
                        p += 1
                        q -= 1
                    p += 1
                    q -= 1

                elif nums[p]+nums[q]<t:
                    p += 1
                else:
                    q -= 1
            return ans
        ans = []
        while i<n:
            if i+2>=n: return ans
            num = nums[i]
            pairs = two_sum(i+1,n-1,-(num))
            # print(pairs)
            if pairs != []:
                for pair in pairs:
                    ans.append([num] + pair)
            while i+1<n and nums[i+1] == nums[i]:
                i += 1
            i += 1
        return ans

        
        