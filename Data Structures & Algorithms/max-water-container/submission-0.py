class Solution:
    def maxArea(self, heights: List[int]) -> int:
        head = 0
        tail = len(heights) - 1
        max_value = 0

        while head != tail:
            value = (tail - head) * min(heights[head], heights[tail])
            if value > max_value:
                max_value = value

            if heights[head] > heights[tail]:
                tail -= 1
            else:
                head += 1

        return max_value    