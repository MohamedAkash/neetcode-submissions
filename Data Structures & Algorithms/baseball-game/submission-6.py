class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []
        for n in operations:
            if n == '+':
                plus = stck[-1] + stck[-2]
                stck.append(plus)
            elif n == 'D':
                mult = stck[-1] * 2
                stck.append(mult)
            elif n == 'C':
                stck.pop()
            else:
                stck.append(int(n))
        return sum(stck)