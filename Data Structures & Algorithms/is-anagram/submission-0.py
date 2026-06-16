class Solution:
    def increaseLetterNumber(self, dic, letter):
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1

        return dic

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_dict = {}
            t_dict = {}
            for idx in range(len(s)):
                s_dict = self.increaseLetterNumber(s_dict, s[idx])
                t_dict = self.increaseLetterNumber(t_dict, t[idx])

            for key in s_dict:
                if not key in t_dict:
                    return False
                else:
                    if s_dict[key] != t_dict[key]:
                        return False

            return True

        else:
            return False