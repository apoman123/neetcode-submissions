class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total_result = []
        buffer = []

        def selection(layer):
            if layer == len(nums):
                total_result.append(buffer.copy())
                return
            else:
                buffer.append(nums[layer])
                selection(layer+1)
                buffer.pop()
                selection(layer+1)

        selection(0)
        return total_result




