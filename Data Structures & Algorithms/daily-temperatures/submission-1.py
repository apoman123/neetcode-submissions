class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] - temperatures[i] > 0:
                    result.append(j-i)
                    break
            if len(result) != i+1:
                result.append(0)
        return result
                