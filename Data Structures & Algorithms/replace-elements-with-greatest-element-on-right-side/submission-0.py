class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for element in range(len(arr)):
            arr[element] = max(arr[element+1:]) if element != len(arr) - 1 else -1
        return arr 