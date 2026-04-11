class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set(nums)
        if len(nums) != len(hs):
            return True
        return False