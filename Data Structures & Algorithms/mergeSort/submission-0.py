# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._mergeSort(pairs, 0, len(pairs)-1)

    def _mergeSort(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs
        
        m = (e + s) // 2

        self._mergeSort(pairs, s, m)
        self._mergeSort(pairs, m+1, e)

        self.merge(pairs, s, e, m)

        return pairs


    def merge(self, pairs: List[Pair], s: int, e: int, m: int) -> None:
        L = pairs[s: m + 1] # end is exclusive
        R = pairs[m + 1: e + 1] 

        i = 0
        j = 0
        k = s

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1
            