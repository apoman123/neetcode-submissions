class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_eat_hour(pile, rate):
            return pile // rate if pile % rate == 0 else  (pile // rate) + 1

        def calc_total_hour(piles, rate):
            total_hour = 0
            for pile in piles:
                total_hour += calc_eat_hour(pile, rate)
            return total_hour

        def binary_search(head, tail):
            middle = (head+tail) // 2
            if head == tail:
                return head
            elif calc_total_hour(piles, middle) > h:
                return binary_search(middle+1, tail)
            elif calc_total_hour(piles, middle) <= h:
                return binary_search(head, middle)
        return binary_search(1, max(piles))
