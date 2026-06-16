class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_alphabets(string):
            alphabets = {}
            for char in string:
                if not char in alphabets:
                    alphabets[char] = 1
                else:
                    alphabets[char] += 1

            return alphabets

        alphabet_list = []
        return_list = []
        for string in strs:
            alphabets = count_alphabets(string)
            if not alphabets in alphabet_list:
                alphabet_list.append(alphabets)
                return_list.append([string])
            else:
                idx = alphabet_list.index(alphabets)
                return_list[idx].append(string)
        
        return return_list


        return total_results