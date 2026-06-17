class Solution:
    def rob(self, nums: List[int]) -> int:
        # max_money[i] = max(max_money[i - 2] + nums[i], max_money[i-1])
        if len(nums) > 1:
            max_money = [0 for i in range(len(nums))]
            max_money[0] = nums[0]
            max_money[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                max_money[i] = max(max_money[i - 2] + nums[i], max_money[i-1])

            return max_money[-1]
        else:
            return nums[0]
