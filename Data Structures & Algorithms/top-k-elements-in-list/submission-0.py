class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_map = Counter(nums)
        for item in freq_map.items():
            heapq.heappush(heap, [-item[1], item[0]])
        # print(heap)
        ans = []
        while heap and k:
            top  = heapq.heappop(heap)
            ans.append(top[1])
            k -= 1
        return ans

            
        