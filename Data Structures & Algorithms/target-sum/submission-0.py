class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_ways = []
        self.current_way = []

        def update_current_way(idx, target):
            if idx == len(nums):
                if sum(self.current_way) == target:
                    total_ways.append(self.current_way)
                    return
                else:
                    return
            else:
                self.current_way.append(nums[idx])
                update_current_way(idx+1, target)
                self.current_way.pop()
                self.current_way.append(nums[idx] * -1)
                update_current_way(idx+1, target)
                self.current_way.pop()
                return 




        update_current_way(0, target)

        if total_ways:
            return len(total_ways)
        else:
            return 0