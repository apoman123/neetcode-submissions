class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = -float("inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) > max_value:
                    max_value = sum(nums[i:j+1])

        return max_value
