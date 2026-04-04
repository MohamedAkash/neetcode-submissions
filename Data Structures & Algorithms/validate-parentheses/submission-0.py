class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hshmap = {'}':'{',')':'(',']':'['}

        for i in s:
            if i in hshmap:
                if stk and hshmap[i] == stk[-1]:
                    stk.pop()
                    continue
                else:
                    return False
            stk.append(i)
        return True if not stk else False