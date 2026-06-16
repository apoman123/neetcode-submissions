class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total_result = []
        global buffer
        buffer = []

        def selection():
            global buffer
            if sum(buffer) == target:
                for result in total_result:
                    if sorted(result) == sorted(buffer.copy()):
                        return
                total_result.append(buffer.copy())
                return

            elif sum(buffer) > target:
                return 
            else:
                for num in nums:
                    buffer.append(num)
                    selection()
                    buffer.pop()
        
        selection()
        return total_result