class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        smaller = defaultdict(list)
        bigger = defaultdict(list)

        for q in queries:
            for interval in intervals:
                if interval[0] <= q:
                    smaller[q].append( (interval[1]- interval[0] + 1, tuple(interval)))
                if interval[1] >= q:
                    bigger[q].append((interval[1]- interval[0] +1, tuple(interval)))

        sol = []
        for q in queries:

            ref = list(set.intersection(set(smaller[q]), set(bigger[q])))
            if ref == []:
                sol.append(-1)
            else:
                heapq.heapify(ref)
                sol.append(heapq.heappop(ref)[0])


        return sol