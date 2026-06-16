class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        total_result = []
        global buffer
        buffer = []

        def selection(idx):
            global buffer
            if idx == len(candidates):
                if sum(buffer) == target:
                    for result in total_result:
                        if sorted(result) == sorted(buffer.copy()):
                            return
                    total_result.append(buffer.copy())
                    return
            else:
                buffer.append(candidates[idx])
                selection(idx+1)
                buffer.pop()
                selection(idx+1)

        selection(0)
        return total_result