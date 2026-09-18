class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        ans = []

        for i, num in enumerate(nums):
            # maintain mono dec queue
            while deq and deq[-1][1]<num:
                deq.pop()
            
            deq.append((i,num))
            
            # maintain window size of k
            while deq and i-deq[0][0]+1>k:
                deq.popleft()
            
            if i>=k-1 and deq:
                ans.append(deq[0][1])
        return ans

        