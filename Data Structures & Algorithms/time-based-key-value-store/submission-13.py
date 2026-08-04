class TimeMap:

    def __init__(self):
        self.store: dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store or self.store[key] == []:
            return ""

        values = self.store[key]
        l, r = 0, len(values) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] < timestamp:
                l = mid + 1
                ans = mid
            elif values[mid][0] > timestamp:
                r = mid - 1
            else:
                return values[mid][1]
        
        return values[ans][1] if values[ans][0] <= timestamp else ""
    

        

