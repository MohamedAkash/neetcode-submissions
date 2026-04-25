class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # brute force: O(n^2)
        # space: O(1)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] and i != j:
        #             return True
        # return False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False