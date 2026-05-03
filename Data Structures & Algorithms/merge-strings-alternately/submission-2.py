class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,j = 0,0
        res = []
        while l <= len(word1) - 1 and j <= len(word2) - 1:
            res.append(word1[l])
            res.append(word2[j])
            l,j = l + 1, j + 1
        res.append(word1[l:])
        res.append(word2[j:])
        return ''.join(res)