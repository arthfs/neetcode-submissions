from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.ref = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ref[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.ref[key])
        self.ref[key] = sorted(self.ref[key], key = lambda x: (x[0]))
        i ,j = 0, n-1
        
        while i<=j:
            m = int( (i+j)/2)
            if self.ref[key] [m] [0] == timestamp:
                return self.ref [key] [m] [1]

            if m == n-1 and self.ref[key][m][0] < timestamp:
                return   self.ref [key] [m][1]

            if self.ref[key][m][0] < timestamp and self.ref[key][m+1][0] > timestamp:
                return self.ref [key] [m][1]

            elif self.ref[key] [m] [0] < timestamp:
                i = m + 1

            elif self.ref[key] [m] [0] > timestamp:
                j = m - 1
           
        return ''  