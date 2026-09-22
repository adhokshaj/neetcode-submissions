class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        l,r = 1, max_rate
        def canEat(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            return time<=h
        ans = float('inf')
        while l<=r:
            mid = (l+r)//2
            if canEat(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans

        