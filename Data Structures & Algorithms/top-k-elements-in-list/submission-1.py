class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        num_freq = dict(Counter(nums))
        # print(num_freq)
        for num,freq in num_freq.items():
            heapq.heappush(heap, [-1*freq,num])
        while k and heap:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans