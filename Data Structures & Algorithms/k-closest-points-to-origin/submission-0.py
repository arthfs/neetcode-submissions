import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ref = []
        for point in points:
            heapq.heappush(ref, ( math.sqrt( (point[0]**2) + (point[1]**2)  ),
             tuple(point)))

        sol = []
        for i in range(k):
            smallest = heapq.heappop(ref)
            sol.append(smallest[1])
        return sol