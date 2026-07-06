

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        def dfs(i):
            if i in dp: return dp[i]
            if i>=n: return 0
            option1 = dfs(i+2) + nums[i]
            option2 = dfs(i+1)
            dp[i] = max(option1, option2)
            return dp[i]
        return dfs(0)

        