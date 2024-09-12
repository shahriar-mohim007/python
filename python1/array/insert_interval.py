def insert(intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        merge = []

        for interval in intervals:
            if not merge or merge[-1][1]<interval[0]:
                merge.append(interval)
            else:
                merge[-1][1] = max(merge[-1][1],interval[1])

        return merge