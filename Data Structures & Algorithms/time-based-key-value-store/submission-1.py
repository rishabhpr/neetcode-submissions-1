class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        values = self.hashmap[key]
        res = ""
        for t, v in values:
            if t <= timestamp:
                res = v
            else:
                break
        return res