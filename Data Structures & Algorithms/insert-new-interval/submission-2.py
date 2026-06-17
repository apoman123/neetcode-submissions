class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def isOverlapped(interval, newInterval):
            if interval[1] >= newInterval[0] and interval[0] < newInterval[0]:
                return True
            if interval[0] <= newInterval[1] and interval[0] > newInterval[0]:
                return True
            if interval[0] <= newInterval[0] and interval[1] >= newInterval[1]:
                return True
            if interval[0] >= newInterval[0] and interval[1] <= newInterval[1]:
                return True
            return False
        
        def combine(overlapped):
            min_value = min([min(lapping) for lapping in overlapped] + [newInterval[0]])
            max_value = max([max(lapping) for lapping in overlapped] + [newInterval[1]])
            return [min_value, max_value]
                
            
        overlapped = []
        for i in range(len(intervals)):
            if isOverlapped(intervals[i], newInterval):
                overlapped.append(intervals[i])

        for interval in overlapped:
            intervals.remove(interval)
        
        

        if overlapped:
            newInterval = combine(overlapped)
        

        # insertion
        if not intervals:
            return [newInterval]

        for i in range(len(intervals)):
            if newInterval[-1] < intervals[i][-1] and intervals:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                break

        if intervals[-1][-1] < newInterval[0]:
            intervals = intervals + [newInterval]

        return intervals 


        