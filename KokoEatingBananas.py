class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min_eating_hours = len(piles)
        # odejmujemy min od kazdego, to jest k
        # pozniej
        # k = max z tego co zostanie / godzine
        if max(piles) == 0:
            return 0

        for k in range(1, max(piles) + 1):
            total_hours = 0
            for e in range(len(piles)):
                total_hours += int(math.ceil(piles[e] / k))
            if total_hours <= h:
                return k

'''
after another 40 minutes of figuring how to define target, mid and low/high
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        target = h
        last_ok = -1
        while L <= R:
            mid = (L + R) // 2
            if helpFun(piles, h, mid) > target: # nie jest ok
                L = mid + 1
            elif helpFun(piles, h, mid) <= target: # jest ok
                R = mid - 1
                last_ok = mid
            # else: # jest idealnie na 100%
            #     return mid

        return last_ok

def helpFun(piles, h, k):
    X = 0
    for i in range(len(piles)):
        X += math.ceil(piles[i] / k)

    return X

