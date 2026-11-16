class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # PREPROCESSING
        s1l = [0] * 26
        for c in s1:
            s1l[ord(c) - ord("a")] += 1

        R = len(s1) - 1
        L = 0
        s2l = [0] * 26

        for i in range(L, R + 1):
            ch = ord(s2[i]) - ord("a")
            s2l[ch] += 1

        if s2l == s1l:
            return True

        while R < len(s2) - 1:
            chL = ord(s2[L]) - ord("a")
            s2l[chL] -= 1

            L += 1
            R += 1

            chR = ord(s2[R]) - ord("a")
            s2l[chR] += 1

            if s2l == s1l:
                return True

        return False
