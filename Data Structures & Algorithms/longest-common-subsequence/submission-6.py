class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        make len(text1) > len(text2)
        s[i][j] = s[i-1][j-1]+1 , if text1[i] == text2[j]
        s[i][j] = max(s[i-1][j], s[i][j-1]), if text1[i] != text[j]
        '''
        lcs = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        # initialization
        # for i in range(len(text1)):
        #     lcs[i][0] = 1 if text2[0] in text1[:i] else 0
        # for j in range(len(text2)):
        #     lcs[0][j] = 1 if text1[0] in text2[:j] else 0

        # if text1[0] == text2[0]:
        #     lcs[0][0] = 1

        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        return lcs[-1][-1]

            