class Solution:
    def binary_search(self, nums, target, head, tail):
        medium = (head + tail) // 2 + 1  if (head + tail) % 2 == 1 else (head + tail) // 2
        if head > tail:
            return -1
        if target == nums[medium]:
            return medium
        elif target > nums[medium]:
            return self.binary_search(nums, target, medium+1, tail)
        elif target < nums[medium]:
            return self.binary_search(nums, target, head, medium-1)
        
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1 
        return self.binary_search(nums, target, head, tail)
    # def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
    #     if l > r:
    #         return -1
    #     m = l + (r - l) // 2

    #     if nums[m] == target:
    #         return m
    #     if nums[m] < target:
    #         return self.binary_search(m + 1, r, nums, target)
    #     return self.binary_search(l, m - 1, nums, target)

    # def search(self, nums: List[int], target: int) -> int:
    #     return self.binary_search(0, len(nums) - 1, nums, target)
        
