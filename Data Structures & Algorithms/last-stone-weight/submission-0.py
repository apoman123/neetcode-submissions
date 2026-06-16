class Solution:
    def smashing(self, stones):
        if len(stones) == 1:
            return stones[-1]
        elif len(stones) == 0:
            return 0
        else:
            first = stones.pop()
            second = stones.pop()
            if first == second:
                return self.smashing(stones)
            else:
                stones.append(first - second)
                stones.sort()
                return self.smashing(stones)


    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        return self.smashing(stones)

        