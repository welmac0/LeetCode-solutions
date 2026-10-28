class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: #O(n)
        # n + y = target
        map = {}
        for i in range(len(nums)):
            n = nums[i]
            #if map.get(target - n): <--- Returning map[x] = 0 and if failed # target > n
            if (target - n) in map:
                return [map[target-n], i]
            else: 
                map[n] = i
                
print(Solution.twoSum(Solution, nums=[2, 7, 11, 15], target=9))