class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            length = 1
            if num-1 not in nums_set: # Leftmost
                while num+1 in nums_set:
                    length += 1
                    num += 1
            ans = max(ans, length)
        return ans
