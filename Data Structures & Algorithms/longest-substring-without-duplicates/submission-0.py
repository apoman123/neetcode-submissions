class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            chars = set()
            current_length = 0
            for j in range(i, len(s)):
                if not s[j] in chars:
                    chars.add(s[j])
                    current_length += 1
                else:
                    break
            if current_length > longest:
                longest = current_length
        return longest