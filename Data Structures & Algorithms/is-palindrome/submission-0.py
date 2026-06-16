import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove spaces and punchuations
        s = s.replace(" ", "").lower()
        s = re.sub(r'[^\w\s]', '', s)
        
        string_stack = []
        result_string = []
        if s:
            for char in s:
                string_stack.append(char)
            
            while len(string_stack) != 0:
                result_string.append(string_stack.pop())

            result_string = ''.join(result_string)
            if result_string == s:
                return True
            else:
                return False
        else:
            return True