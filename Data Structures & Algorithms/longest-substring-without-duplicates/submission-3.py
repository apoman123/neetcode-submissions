class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check_sub(sub):
            chars = set()
            for char in sub:
                if char in chars:
                    return False
                else:
                    chars.add(char)
            return True


        max_len = 0
        for size in range(1, len(s)+1):
            for j in range(len(s)+1-size):
                if check_sub(s[j:j+size]) and size > max_len:
                    max_len = size
        return max_len

                    


        