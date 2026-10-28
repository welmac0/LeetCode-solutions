class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # O(n)
        dictS = {}
        dictT = {}
        for c in s: # O(n)
            # if c in dictS: # same as dictS.keys() O(1)
            #     dictS[c] += 1
            # else:
            #     dictS[c] = 1
            dictS[c] = dictS.get(c, 0) + 1
        
        for c in t: # O(n)
            # if c in dictT: 
            #     dictT[c] += 1
            # else:
            #     dictT[c] = 1
            dictT[c] = dictT.get(c, 0) + 1 # O(1)
            # works as above; get(c, 0) = get(c) or dictT[c] = 0
            # speeds up

        if dictS == dictT: #O(n)
            return True

        return False