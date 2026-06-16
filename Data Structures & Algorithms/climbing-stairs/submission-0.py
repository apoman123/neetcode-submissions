class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0, 1, 2] + [1 for i in range(28)]
        for i in range(3, 31):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]
