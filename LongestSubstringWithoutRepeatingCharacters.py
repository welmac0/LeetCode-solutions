"""
done in 18 minutes in two tries.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        L = 0
        longest = -1
        sset = set()
        for R in range(len(s)):
            if s[R] not in sset:
                sset.add(s[R])
            else:
                # longest = max(longest, len(sset))
                while s[R] in sset:
                    sset.remove(s[L])
                    L += 1
                sset.add(s[R])
            longest = max(longest, len(sset))

        return longest
