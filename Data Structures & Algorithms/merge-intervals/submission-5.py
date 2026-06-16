class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def quick_sort(intervals):
            if not intervals:
                return intervals
            else:
                pivot = len(intervals) // 2
                front_intervals = []
                back_intervals = []
                for idx in range(len(intervals)):
                    if idx != pivot:
                        if intervals[idx][0] < intervals[pivot][0]:
                            front_intervals.append(intervals[idx])
                        elif intervals[idx][0] == intervals[pivot][0] and intervals[idx][1] < intervals[pivot][1]:
                            front_intervals.append(intervals[idx])
                        else:
                            back_intervals.append(intervals[idx])
                return quick_sort(front_intervals) + [intervals[pivot]] + quick_sort(back_intervals)

        if intervals:
            intervals = quick_sort(intervals)
            print(intervals)
            result = [intervals[0]]
            for i in range(1, len(intervals)):
                if result[-1][1] >= intervals[i][0]:
                    start, end = result.pop()
                    new_end = max(end, intervals[i][1])
                    result.append([start, new_end])
                else:
                    result.append(intervals[i])
            return result
        else:
            return intervals
            
            