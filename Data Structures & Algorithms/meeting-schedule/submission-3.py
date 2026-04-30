"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals = sorted(intervals, key = lambda x : (x.start, x.end) )
        if intervals == []:
            return True

        ref = [intervals.pop(0)]
        for i in intervals:
            if i.start < ref[-1].end:
                return False
            ref.append(i)

        return True
 