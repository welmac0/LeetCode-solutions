class Solution:
    def productExceptSelf(
        self, nums: List[int]
    ) -> List[
        int
    ]:  # nie chcialem tego robic, ale nie wiedzialem jak sumy prefixowe tu uzyc :( Lepsze male cos niz wielke nic
        # bruteforce
        n = len(nums)
        ret_l = [1] * n
        for i in range(n):  # liczby
            for j in range(n):  # pozycje tablicy
                if i != j:
                    ret_l[i] *= nums[j]

        return ret_l


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        base = [1] * len(nums)
        preA = base.copy()
        for i in range(1, len(nums)):
            preA[i] = preA[i - 1] * nums[i - 1]

        sufA = base.copy()
        for i in range(
            len(nums) - 2, -1, -1
        ):  # n-2 (last index is n-1), to -1 (won't get there), by -1 every iteration
            sufA[i] = sufA[i + 1] * nums[i + 1]

        ret_l = base.copy()
        for i in range(0, len(nums)):
            ret_l[i] = preA[i] * sufA[i]

        return ret_l


"""
ogolny pomysl, np: [-1 0 1 2 3]
prefix: [1 -1 0 0 0]
suffix: [0 6 6 3 1]
vector product (v_i * w_i) = [0 -6 0 0 0] gotowe.

"""
