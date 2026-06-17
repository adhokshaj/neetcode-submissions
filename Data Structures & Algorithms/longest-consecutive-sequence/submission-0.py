class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxx = 0
        for num in nums:
            if num-1 not in nums_set:
                #This is the edge number
                length = 0
                temp = num
                while temp in nums_set:
                    length +=1
                    temp += 1
                maxx = max(maxx, length)
        return maxx
