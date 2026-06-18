class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        maxx = 0
        while l<r:
            maxx = max(maxx, (r-l)*min(heights[l], heights[r]))
            if heights[l]<heights[r]:
                l += 1
            else:
                r -= 1
        return maxx