class Solution:
    def calc_distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.calc_distance(point, [0,0]), point) for point in points]
        heapq.heapify(distances)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(distances)[1])
        return result