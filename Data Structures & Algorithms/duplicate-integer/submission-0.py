class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        # print(freq)
        for num, count in freq.items():
            if count>1:
                return True
        return False
        