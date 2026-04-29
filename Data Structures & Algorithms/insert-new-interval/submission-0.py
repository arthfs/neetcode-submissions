class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ref = []
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        ref.append(intervals.pop(0))

        for i in intervals:
            if i[0] <= ref[-1] [1]:
                ref[-1] = [ min( [i[0], ref[-1] [0]] ), max([ i[1], ref[-1] [1] ])]
            else:
                ref.append(i)

        return ref