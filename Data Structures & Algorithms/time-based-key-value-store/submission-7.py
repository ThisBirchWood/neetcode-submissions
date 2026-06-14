class TimeMap:

    def __init__(self):
        self.data = {

        }

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        history = self.data[key]

        l = 0
        r = len(history) - 1
        m = 0

        while l <= r:
            m = (l + r) // 2

            if history[m][1] > timestamp:
                r = m - 1
            elif history[m][1] < timestamp:
                l = m + 1
            else:
                return history[m][0]

        if timestamp < history[r][1]:
            return ""

        return history[r][0]
        
