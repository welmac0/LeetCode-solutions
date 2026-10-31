class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums_sorted = sorted(nums)
        triplets: List[List[int]] = []
        for i in range(n):
            # Two Pointers
            L = 0
            R = n - 1
            while L < R:
                if L == i:
                    L += 1
                if R == i:
                    R -= 1
                if L == R:
                    break

                s = nums_sorted[L] + nums_sorted[R] + nums_sorted[i]
                if s < 0:
                    L += 1
                elif s > 0:
                    R -= 1
                else:
                    triplets.append([nums_sorted[L], nums_sorted[R], nums_sorted[i]])
                    L += 1
                    R -= 1

        unique_triplets = [list(t) for t in set(tuple(sorted(x)) for x in triplets)]
        return unique_triplets
