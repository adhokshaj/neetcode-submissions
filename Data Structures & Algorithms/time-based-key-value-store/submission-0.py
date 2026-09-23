class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store[key]
        n = len(entries)
        l,r = 0, n-1
        ans = ''
        while l<=r:
            mid = (l+r)//2
            t, val = entries[mid]
            if t==timestamp:
                return val
            elif t<timestamp:
                ans = val
                l = mid+1
            else:
                r = mid-1
        return ans

        
