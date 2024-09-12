def eraseOverlapIntervals(intervals):
        intervals.sort(key=lambda x:x[1])
        second = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] >= second:
                second = intervals[i][1] 
            else:
                count+=1
            
        return count   
               