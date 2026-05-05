class Solution:
    def isValid(self, s: str) -> bool:
        hs = {'}':'{', ']':'[', ')':'('}
        stack = []

        for i in s:
            if i in hs:
                if stack and hs[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
