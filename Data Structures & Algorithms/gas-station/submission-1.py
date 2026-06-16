class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        else:
            for start_idx in range(len(gas)):
                total = 0
                for j in range(len(gas)):
                    total += gas[(start_idx+j) % len(gas)] - cost[(start_idx+j) % len(gas)]
                    if total < 0:
                        break
                        
                if total >= 0:
                    return start_idx
                        

