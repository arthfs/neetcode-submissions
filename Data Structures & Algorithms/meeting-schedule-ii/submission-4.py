"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals == []:
            return 0

        intervals = sorted(intervals, key = lambda x : (x.start, x.end))
        ref = [[intervals.pop(0)]]
        
        for i in intervals:
            for j in ref:
                if i.start >= j[-1].end:
                    j.append(i)
                    break
            else:
                ref.append([i])

        return len(ref)