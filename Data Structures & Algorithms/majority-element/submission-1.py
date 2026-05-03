class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hs = defaultdict(int)
        for i in nums:
            hs[i] = hs[i] + 1
        
        for i, n in hs.items():
            if n > len(nums) // 2:
                return i
            