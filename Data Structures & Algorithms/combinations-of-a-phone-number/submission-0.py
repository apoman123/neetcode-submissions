class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        else:
            mapping = {
                '2': "abc", 
                '3': "def",
                '4': "ghi",
                '5': "jkl",
                '6': "mno",
                '7': "pqrs",
                '8': "tuv",
                '9': "wxyz"
                }

            total_result = []
            letters = [mapping[digit] for digit in digits]
            global buffer
            buffer = ""

            def selection(layer):
                global buffer
                if layer == len(letters):
                    total_result.append(buffer)
                else:
                    for letter in letters[layer]:
                        buffer = buffer + letter
                        selection(layer+1)
                        buffer = buffer[:-1]
            
            selection(0)

            return total_result
                    