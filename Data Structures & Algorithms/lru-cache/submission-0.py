import heapq
class LRUCache:

    def __init__(self, capacity: int):
        self.n = 0
        self.ref = dict()
        self.cap = capacity
        self.timestamp = 0
        self.heap = []

    def get(self, key: int) -> int:
        item = self.ref.get(key, -1)
        if item == -1:
            return -1
        
        self.ref[key] [0] = self.timestamp
        heapq.heappush(self.heap, (self.timestamp, key) )
        self.timestamp+=1
        return item[1]

    def put(self, key: int, value: int) -> None:
        if self.ref.get(key)!= None:
            self.ref[key] [1] = value
            self.ref[key] [0] = self.timestamp
            heapq.heappush(self.heap, (self.timestamp, key) )
            

        elif self.n < self.cap:
            self.ref[key] = [self.timestamp, value]
            heapq.heappush(self.heap, (self.timestamp, key) )
            self.n+=1

        else:
            
            while self.heap!=[]:
                lru = heapq.heappop(self.heap)
                lru_info = self.ref.get(lru[1])
                if lru_info == None:
                    continue

                if lru_info [0] == lru[0]:
                    self.ref[ key ] = [self.timestamp, value]
                    heapq.heappush(self.heap, (self.timestamp, key) )
                    del self.ref[lru[1]]
                    break
           
        
        self.timestamp+=1

