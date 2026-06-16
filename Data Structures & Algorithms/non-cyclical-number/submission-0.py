import math
class Solution:
    def isHappy(self, n: int) -> bool:
        def parse_numbers(num):
            stack = []
            parsed = []
            while num:
                stack.append(num % 10)
                num = num // 10
            
            while stack:
                parsed.append(stack.pop())

            return parsed

        exist_result = set()
        while True:
            temp_result = 0
            parsed = parse_numbers(n)
            for digit in parsed:
                temp_result += digit * digit
            if temp_result == 1:
                return True
            elif temp_result in exist_result:
                return False
            elif not temp_result in exist_result:
                exist_result.add(temp_result)
            n = temp_result
