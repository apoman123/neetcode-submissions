class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # discard greater
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                triplets.remove(triplet)
        
        def in_triple_with_pos(num, triplet, pos):
            return True if triplet[pos] == num else False

        
        for pos, val in enumerate(target):
            has_element = False
            for triplet in triplets:
                if in_triple_with_pos(val, triplet, pos):
                    has_element = True

            if not has_element:
                return False
        
        return True

            

        
        