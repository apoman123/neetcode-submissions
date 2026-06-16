class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_dict = {}
        for idx, element in enumerate(nums):
            if idx == 0:
                temp_dict[str(element)] = ""
            else:
                if str(element) in temp_dict:
                    return True
                else:
                    temp_dict[str(element)] = ""
                
        return False
        