class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)  # O(1)
        L = 0
        R = n - 1
        v_max = 0
        while L < R:
            v_max = max(v_max, (R - L) * min(heights[L], heights[R]))

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return v_max


"""
My initial approach was almost perfect, except instead of
`if heights[L] < heights[R]`
I did
`if heights[L + 1] > heights[R - 1]`
what was wrong. I got final answer by hints at the point
I was sure I won't come with something better. 
30 mins.
"""
