class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l,r = 0,k
        n = len(nums)
        
        for i in range(k):
            while queue and queue[-1][1] < nums[i]:
                queue.pop()
            queue.append([i,nums[i]])

        ans = []

        while r<=n:

            # print(queue)

            # pop all the numbers out of window
            while queue[0][0]<l:
                queue.popleft()

            # now the window is valid
            if queue: ans.append(queue[0][1])
            
            # add the current number
            while r<n and queue and queue[-1][1] < nums[r]:
                queue.pop()
            if r<n: queue.append([r,nums[r]])

            l += 1
            r += 1
        
        return ans

        