class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = set()
        for num in nums:
            if num in single:
                single.remove(num)
            else:
                single.add(num)
            
        return single.pop()