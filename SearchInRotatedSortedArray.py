class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        t = target
        while L <= R:
            m = (L + R) // 2

            if nums[m] == t:
                return m

            if nums[L] <= nums[m]:
                # middle nalezy do left sorted portion
                if t > nums[m] or t < nums[L]:
                    # P1. np. dobrze posortowane
                    # P2. urywa sie za m
                    L = m + 1
                else:
                    # L < t < M
                    R = m - 1
            else:
                # middle nalezy do right sorted portion
                if t < nums[m] or t > nums[R]:
                    # P1. no bo wiemy ze t < nums[m] <= nums[R]
                    # P2. t jest wieksze niz r, czyli jw
                    R = m - 1
                else:
                    L = m + 1

        return -1


"""
This one was super hard for me. Spent about 2h in total and couldn't figure it out anyway.
"""
