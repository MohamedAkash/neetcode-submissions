class Solution:
    def isValid(self, s: str) -> bool:
        hs = {'}':'{', ']':'[', ')':'('}
        stack = []

        for c in s:
            if c in hs:
                if stack and hs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
