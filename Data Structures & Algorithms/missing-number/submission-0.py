class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for idx in range(len(nums)+1):
            if not idx in nums:
                return idx
