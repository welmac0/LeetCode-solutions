class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        if nums[L] < nums[R]:
            return nums[L]

        while L <= R:
            m = (L + R) // 2

            if R - L < 2:
                return min(nums[L], nums[R])

            if nums[L] > nums[m]:
                R = m
            elif nums[m] > nums[R]:
                L = m


"""
done in like 15 minutes. Pretty similar to bisection method in problem of looking roots in function.
"""
