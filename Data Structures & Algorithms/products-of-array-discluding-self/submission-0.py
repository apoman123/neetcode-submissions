class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def find_zero_idx(nums):
            idxes = []
            for idx in range(len(nums)):
                if nums[idx] == 0:
                    idxes.append(idx)
            return idxes

        if len(find_zero_idx(nums)) >= 2:
            return [0 for _ in range(len(nums))]
        else:
            output = []
            for i in range(len(nums)):
                value_for_idx_i = 1
                for j in range(len(nums)):
                    if j != i:
                        value_for_idx_i *= nums[j]
                output.append(value_for_idx_i)
            return output


