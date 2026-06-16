import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        num = None
        for _ in range(k):
            num = heapq.heappop_max(nums)
        
        return num