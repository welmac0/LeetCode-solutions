import re

def isPalindrome(s: str) -> bool:
        # two pointers
        s_checked = s.lower()
        s_checked = re.sub(r'[^a-zA-Z0-9]', '', s_checked) # regex is super slow
        L = 0
        R = len(s) - 1
        while L < R:
            print(f"L: {s[L]}, R: {s[R]}")
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1

        return True
    
print(isPalindrome(s="Was it a car or a cat I saw?"))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        s_checked = s.lower()
        L = 0
        R = len(s_checked) - 1
        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            if s_checked[L] != s_checked[R]:
                return False
            else:
                L += 1
                R -= 1

        return True