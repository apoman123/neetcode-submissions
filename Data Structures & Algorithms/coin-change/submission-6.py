
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        else:
            if amount < min(coins):
                return -1

            cost = [None for _ in range(amount+1)]
            cost[0] = 0

            #initialize
            for coin in coins:
                if coin in range(amount+1):
                    cost[coin] = 1
            
            for idx in range(amount+1):
                if cost[idx] == None:
                    current_cost = float("inf")
                    for coin in coins:
                        if (idx - coin) in range(amount+1) and current_cost > cost[idx-coin] + 1:
                            current_cost = cost[idx-coin] + 1
                    cost[idx] = current_cost
            print(cost)
            return cost[-1] if cost[-1] != float("inf") else -1
                


             

