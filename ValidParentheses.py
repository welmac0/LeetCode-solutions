class Solution:  # ~ 10 minutes
    def isValid(self, s: str) -> bool:
        stack = []  # wskaznik na stack: s_len - 1
        for b in s:
            if b in ["(", "{", "["]:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                elif (
                    (b == ")" and stack[-1] == "(")
                    or (b == "]" and stack[-1] == "[")
                    or (b == "}" and stack[-1] == "{")
                ):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True

        return False
