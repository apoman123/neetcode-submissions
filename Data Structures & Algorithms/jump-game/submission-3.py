class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        idx = goal - 1

        while idx >= 0:
            if nums[idx] >= goal - idx:
                goal = idx
            idx -= 1 
        
        if goal == 0:
            return True
        else:
            return False