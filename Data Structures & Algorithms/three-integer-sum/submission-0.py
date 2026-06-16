class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    addition = [nums[i], nums[j], nums[k]]
                    addition.sort()
                    if nums[i] + nums[j] + nums[k] == 0 and i < j < k and not addition in result:
                        result.append(addition)
        return result