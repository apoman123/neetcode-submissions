class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        empty_str = ""
        for digit in digits:
            empty_str += str(digit)
        out_list = []
        for char in str(int(empty_str) + 1):
            out_list.append(int(char))
        return out_list