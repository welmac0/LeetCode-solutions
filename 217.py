class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hs = set()
        for n in nums: # O(n)
            x = len(hs) # O(1)
            hs.add(n) # O(1)
            if len(hs) == x: # O(1)
                return True
        
        return False
    
# version 2
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums: # O(n)
            if n in seen: # O(1)
                return True
            seen.add(n) # O(1)
        
        return False