class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. Here first pick a day as if you are buying on that day
        # 2. While traversing if the price on that day is more than
        #    the day you bought its good so calculate the profit on 
        #    each day where the price is greater
        # 3. When you're at a day where price is less than the day you
        #    you bought, it's better to think of buying today(because we
        #    already have the max profit we can get till now with a day 
        #    whose price is greater than today if there is any day in 
        #    future with more price its better to buy today rather than the
        #    previous day)
        # 4. continue the same process till last day

        bought_day = 0
        cur_day = bought_day+1
        n = len(prices)
        profit = 0
        while cur_day<n:
            if prices[cur_day]<prices[bought_day]:
                bought_day = cur_day
                continue
            profit = max(profit, prices[cur_day]-prices[bought_day])
            cur_day += 1
        return profit
        