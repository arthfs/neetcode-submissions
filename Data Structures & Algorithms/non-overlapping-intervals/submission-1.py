class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ref = []
        sol = 0 

        intervals = sorted(intervals, key = lambda x : (x[1] , x[0]) )
      
        ref.append(intervals.pop(0))
        for i in intervals:
            if i[0] < ref[-1] [1] :
                sol+=1
            else:
                ref.append(i)

       
        return sol    