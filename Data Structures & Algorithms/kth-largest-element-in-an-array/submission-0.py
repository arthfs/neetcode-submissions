import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ref = []
        for i in nums:
            if len(ref)!=k:
                heapq.heappush(ref, i)
            else:
                top = heapq.heappop(ref)
                if i > top:
                    heapq.heappush(ref, i)
                else:
                    heapq.heappush(ref, top)
        return heapq.heappop(ref)