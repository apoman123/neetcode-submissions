class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            # s[k] = max(s[k-1], s[k-2]+nums[k])
            best_value = [nums[0], max(nums[0], nums[1])] + [0 for _ in range(len(nums) - 2)]
            for idx in range(2, len(nums)):
                best_value[idx] = max(best_value[idx-1], best_value[idx-2] + nums[idx])
            return best_value[-1]
        