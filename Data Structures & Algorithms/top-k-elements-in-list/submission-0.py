from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = Counter(nums)
        items = list(ref.items())
        queue = []
   
        for i in range(k):
            item = items.pop(0)
            heapq.heappush(queue, (item[1], item[0]))

        for i in items:
            top = heapq.heappop(queue)
            if i[1] > top[0]:
                heapq.heappush(queue, (i[1], i[0]))
            else:
                heapq.heappush(queue, top)
        
        sol = []
        while queue!= []:
            sol.append(heapq.heappop(queue) [1])

        return sol