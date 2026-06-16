class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_list = []
        for idx, element in enumerate(nums):
            if idx == 0:
                temp_list.append(element)
            else:
                if element in temp_list:
                    return True
                else:
                    temp_list.append(element)
                
        return False
        