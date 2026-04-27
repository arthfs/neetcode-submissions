import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ref = []
        for s in stones:
            heapq.heappush(ref, -s)

        while ref!=[]:
            try:
                x = heapq.heappop(ref)
                y = heapq.heappop(ref)

                if abs(x) < abs(y):
                    heapq.heappush(ref, - (abs(y) - abs(x) ) )

                elif abs(x) > abs(y):
                    heapq.heappush(ref, - (abs(x) - abs(y) ))
            except:
                return -x
        return 0
        
