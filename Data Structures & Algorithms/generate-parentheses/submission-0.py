from copy import copy
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(parentheses):
            stack = []
            for parenthes in parentheses:
                stack.append(parenthes)
                if len(stack) >= 2 and stack[-1] == ")" and stack[-2] == "(":
                    stack.pop()
                    stack.pop()
            if stack:
                return False
            else:
                return True

        total_result = []
        global buffer
        buffer = []
        max_steps = n * 2

        def selection(step):
            global buffer
            if step == max_steps:
                total_result.append(buffer.copy())
                return 
            else:
                buffer.append("(")
                selection(step+1)
                buffer.pop()
                buffer.append(")")
                selection(step+1)
                buffer.pop()


        selection(0)

        return [''.join(parenthes) for parenthes in total_result if is_valid(parenthes)]
            
            
