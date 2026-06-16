class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)  == 1:
            return nums[0]    
        else:
            def robbing(array):
                if len(array) == 1:
                    return array[0]
                else:
                    result = [None for _ in range(len(array))]
                    # initialize
                    result[0] = array[0]
                    result[1] = max(array[0], array[1])

                    for i in range(2, len(array)):
                        result[i] = max(result[i-1], array[i]+result[i-2])

                    return result[-1]
            return max(robbing(nums[:-1]), robbing(nums[1:]))

