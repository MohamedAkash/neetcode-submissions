class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = {']':'[', ')':'(', "}":'{'}
        stck = []
        
        for c in s:
            if c in valid:
                if stck and stck[-1] == valid[c]:
                    stck.pop()
                else:
                    return False
            else:
                stck.append(c)
        return True if not stck else False
            


