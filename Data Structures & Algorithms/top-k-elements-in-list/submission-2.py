class Solution:
    def quick_sort(self, pair_list):
        if not pair_list:
            return pair_list 
        else:
            less = []
            more = []
            pivot = len(pair_list) // 2 - 1if len(pair_list) % 2 == 0 else len(pair_list) // 2
            for idx in range(len(pair_list)):
                if idx != pivot:
                    if pair_list[idx][1] < pair_list[pivot][1]:
                        less.append(pair_list[idx])
                    else:
                        more.append(pair_list[idx])
            return self.quick_sort(less) + [pair_list[pivot]] + self.quick_sort(more)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if str(num) in freq_dict:
                freq_dict[str(num)] += 1
            else:
                freq_dict[str(num)] = 1

        freq_tuples = list(freq_dict.items())
        freq_tuples = self.quick_sort(freq_tuples)
        return [int(freq_tuples[idx][0]) for idx in range(-1, -1-k, -1)]


