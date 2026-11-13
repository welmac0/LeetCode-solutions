class Solution:
    """
    Just watched NeetCode explanation about problem and then done this. It was easy from that point.
    When I tried to do it myself, I couldn't figure out how to get the most frequent letter in O(n) - and I wouldn't figure it out.
    I'd have gone with trying all the letters as keys in the hashmap (which is O(26*n) and it's still valid), but I couldn't bear it.
    So this approach is elegant and I'll have to revise it in the future.
    """

    def characterReplacement(self, s: str, k: int) -> int:
        R = 0
        L = 0
        letters = {}
        maxf = 0
        bestsofar = 0
        while R < len(s):
            c = ord(s[R].lower()) - ord("a")
            letters[c] = letters.get(c, 0) + 1
            maxf = max(letters[c], maxf)
            if (R - L + 1) - maxf <= k:
                bestsofar = max(bestsofar, R - L + 1)
            else:
                while (R - L + 1) - maxf > k:
                    c = ord(s[L].lower()) - ord("a")
                    letters[c] -= 1
                    L += 1

            R += 1

        return bestsofar
