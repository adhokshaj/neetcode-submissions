class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def dfs(i, cur):
            if i==n: 
                temp = cur[:]
                ans.append(temp)
                return

            cur.append(nums[i])
            dfs(i+1, cur)

            cur.pop()
            dfs(i+1, cur)

            return
        dfs(0, [])
        return ans
            

        