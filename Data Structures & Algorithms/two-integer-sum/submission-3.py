class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past_differences = {}
        for idx in range(len(nums)):
            difference = target - nums[idx]
            if difference in past_differences:
                return [past_differences[difference], idx]
            else:
                past_differences[nums[idx]] = idx