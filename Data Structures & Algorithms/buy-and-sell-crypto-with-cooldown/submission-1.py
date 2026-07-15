from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        #max profit I can achieve on day i based on my previous day
        @cache
        def dfs(i, bought):
            # print(i,prev_sold_day)
            if i>=n: return 0

            profit = 0


            if not bought:
                #buy
                profit = max(profit, dfs(i+1,True)-prices[i])
            else:
                #sell
                profit = max(profit, dfs(i+2, False)+prices[i])
                
            #skip
            profit = max(profit, dfs(i+1, bought))

            return profit
        return dfs(0, False)



        