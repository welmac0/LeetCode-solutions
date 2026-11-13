class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        wystapienia = {}  # indexy
        for i in range(len(nums)):
            n = nums[i]
            if n in wystapienia:
                wystapienia[n].append(i)
            else:
                wystapienia[n] = [i]

        okKeys = []
        mostFrequent = 0
        for k, v in wystapienia.items():
            if len(v) > mostFrequent:
                mostFrequent = len(v)
                okKeys.clear()
                okKeys.append(k)
            elif len(v) == mostFrequent:
                okKeys.append(k)

        minLen = float("inf")
        for key in okKeys:
            items = wystapienia[key]
            minLen = min(items[-1] - items[0] + 1, minLen)

        return minLen

        return
