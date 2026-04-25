class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for number in nums:
            if number in hset:
                return True
            hset.add(number)
        return False