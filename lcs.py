class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  # 20 minut, n2
        na = list(set(nums))
        n = len(na)

        if len(nums) == 0:
            return 0

        # nlogn
        for i in range(1, n):
            while i > 0 and na[i - 1] > na[i]:
                na[i - 1], na[i] = na[i], na[i - 1]
                i -= 1

        buf = set()
        longest_set = 1
        for i in range(1, n):
            if na[i] - na[i - 1] == 1:
                buf.add(na[i])
                buf.add(na[i - 1])
            else:
                buf = set()
            if len(buf) > longest_set:
                longest_set = len(buf)

        return longest_set


print(
    Solution.longestConsecutive(Solution, nums=[9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7])
)


class Solution:  # z hintami, ok 15 minut. Wypierdalalo mi time complexity, bo mialem nl = list(set(nums)), co niszczylo zlozonosc i nie zauwyazylem teog. Po poprawieniu O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nl = set(nums)
        if len(nl) == 0:
            return 0
        longest = 1

        curr = longest
        for num in nl:
            if num - 1 not in nl:
                curr = 1
                while num + curr in nl:
                    curr += 1
                if curr > longest:
                    longest = curr

        return longest
