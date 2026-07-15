from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dfs(i, cur):
            if cur==amount:
                return 1
            if i==n:
                return 0
            
            #take
            take = 0
            if cur+coins[i]<=amount:
                take = dfs(i, cur+coins[i])

            #dont_take
            dont_take = dfs(i+1, cur)

            return take + dont_take
        
        return dfs(0,0)
        