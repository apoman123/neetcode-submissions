class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.buffer = []
        result = []
        def backtracking():
            if len(self.buffer) == len(nums):
                result.append(self.buffer.copy())
            else:
                for num in nums:
                    if not num in self.buffer: 
                        self.buffer.append(num)
                        backtracking()
                        self.buffer.pop()
                
                    
            

        
        backtracking()
        return result