class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        for i in range(n):
            if i == n - 1: # reached the end of the arr (last element)
                ans[i] = -1
            else: # have not reached last element
                ans[i] = max(arr[i + 1:]) # slice[x:y], x is inclusive, y is exclusive
        return ans