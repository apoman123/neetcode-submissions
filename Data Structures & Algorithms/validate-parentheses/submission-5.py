class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            stack.append(bracket)
            if len(stack) >= 2:
                if stack[-1] == "}" and stack[-2] == "{":
                    stack.pop()
                    stack.pop()

                elif stack[-1] == ")" and stack[-2] == "(":
                    stack.pop()
                    stack.pop()

                elif stack[-1] == "]" and stack[-2] == "[":
                    stack.pop()
                    stack.pop()
            
        if len(stack) != 0:
            return False
        else:
            return True
        