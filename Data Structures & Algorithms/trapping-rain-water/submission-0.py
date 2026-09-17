class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        l_max, r_max = height[0], height[n-1]
        ans = 0
        while l<=r:
            if l_max<r_max:
                l_max = max(l_max, height[l])
                ans += l_max - height[l]
                l += 1
            else:
                r_max = max(r_max, height[r])
                ans += r_max - height[r]
                r -= 1
        return ans



        