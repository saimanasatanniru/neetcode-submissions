class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""
        values = self.key_store[key]
        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res 
