class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # This is a canonical problem of find NGE (monotonic stack - decreasing)

        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                top = stack.pop()
                ans[top[0]] = i - top[0]
            stack.append([i, temp]) 
        return ans
        