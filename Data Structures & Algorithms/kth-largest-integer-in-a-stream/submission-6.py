class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        if len(self.nums) == 0:
            self.nums.append(val)
            return self.nums[-self.k] 
            
        if val <= self.nums[-1] and len(self.nums) != 0:
            for idx in range(len(self.nums)):
                if val <= self.nums[idx]:
                    self.nums.insert(idx, val)
                    break
        else:
            self.nums.append(val)
        return self.nums[-self.k] 
