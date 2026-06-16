"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import math

class Solution:
    def quick_sort(self, intervals:List):
        pivot = math.ceil(len(intervals) // 2)
        if len(intervals) == 0:
            return []
        else:
            less = []
            more = []
            for idx in range(len(intervals)):
                if idx != pivot:
                    if intervals[idx].start < intervals[pivot].start:
                        less.append(intervals[idx])
                    else:
                        more.append(intervals[idx])
            return self.quick_sort(less) + [intervals[pivot]] + self.quick_sort(more)

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = self.quick_sort(intervals)
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if intervals[j].start < intervals[i].end or intervals[j].start == intervals[i].start:
                    return False
        return True
        
