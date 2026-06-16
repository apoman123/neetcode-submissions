class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        cost[i-1][j-1], if word1[i] == word[j]

        min(cost[i-1][j-1]+1, cost[i-1][j]+1, cost[i][j-1]+1), if word[i] != word[j]
        '''

        if word1 and word2:
            cost = [[None for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

            # initialize
            cost[0][0] = 0 
            
            for idx in range(1, len(word2)+1):
                cost[0][idx] = idx

            for idx in range(1, len(word1)+1):
                cost[idx][0] = idx
            # print(cost)

            for i in range(1, len(word1)+1):
                for j in range(1, len(word2)+1):
                    if word1[i-1] == word2[j-1]:
                        cost[i][j] = cost[i-1][j-1]
                    else:
                        cost[i][j] = min(cost[i-1][j-1], cost[i-1][j], cost[i][j-1]) + 1
    
            return cost[-1][-1]
        elif word1 and not word2:
            return len(word1)
        else:
            return len(word2)


        
