class TimeMap:
    def __init__(self):
        self.store: dict[str,list[tuple[int,str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return res
        value = self.store[key]
        left = 0
        right = len(value) - 1

        while left <= right:
            mid = (left + right) // 2
            if value[mid][0] <= timestamp:
                res = value[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res

t = TimeMap()
t.set("alice", "happy", 1)
print(t.get("alice", 1))
print(t.get("alice", 2))
t.set("alice", "sad", 3)
print(t.get("alice", 3))