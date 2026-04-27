import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for i in nums:
            if len(self.nums) < k:
                heapq.heappush(self.nums, i)
            
            else:
                top = heapq.heappop(self.nums)
                if i > top:
                    heapq.heappush(self.nums, i)
                else:
                    heapq.heappush(self.nums, top)

   

    def add(self, val: int) -> int:
        if self.nums == []:
            heapq.heappush(self.nums, val)
            return val

        if len(self.nums) <self.k:
            heapq.heappush(self.nums, val)
        
        else:
            top = heapq.heappop(self.nums)
            if val > top:
                heapq.heappush(self.nums, val)
            
            else:
                heapq.heappush(self.nums, top)
        
        sol = heapq.heappop(self.nums)
        heapq.heappush(self.nums, sol)
        return sol
       
