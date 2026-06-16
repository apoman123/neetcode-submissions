import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_distance(point):
           return math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
        
        dist_point = [(calc_distance(point), point)for point in points]
        heapq.heapify(dist_point)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(dist_point)[-1])

        return result
