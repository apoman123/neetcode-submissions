class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        total_result = []
        buffer = []

        def selection(layer):
            if layer == len(nums):
                for result in total_result:
                    if sorted(result) == sorted(buffer.copy()):
                        return 
                total_result.append(buffer.copy())
                return
            else:
                buffer.append(nums[layer])
                selection(layer+1)
                buffer.pop()
                selection(layer+1)

        selection(0)
        return total_result