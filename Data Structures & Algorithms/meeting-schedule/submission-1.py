"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
def overlap(a,b):
    if b.end<= a.end:
        return True
    if b.start< a.end:
        return True
    return False

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals,key = lambda x : (x.start,x.end) )
        for i in range(len(intervals)-1):
            if overlap(intervals[i],intervals[i+1]):
                return False
        return True