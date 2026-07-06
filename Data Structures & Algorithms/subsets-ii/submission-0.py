class Solution:
    def subsetsWithDup(self, candidates: List[int]) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, cur):
            if i>=n: 
                ans.append(cur.copy())
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur)

            while i+1<n and candidates[i+1]==candidates[i]:
                i += 1
            cur.pop()
            dfs(i+1, cur)

        dfs(0, [])
        return ans
        