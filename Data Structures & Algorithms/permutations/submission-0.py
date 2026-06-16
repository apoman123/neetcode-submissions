class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        total_result = []
        buffer = []

        def selection(layer):
            if layer == len(nums):
                if not buffer in total_result:
                    total_result.append(buffer.copy())
                return
            else:
                for num in nums:
                    if not num in buffer:
                        buffer.append(num)
                        selection(layer+1)
                        buffer.pop()
                
        selection(0)

        return total_result

        