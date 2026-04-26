class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        prefix = strs[0]
        
        for i in range(len(prefix)):
            c = prefix[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    return "".join(ans)
            ans.append(c)
        
        return "".join(ans)