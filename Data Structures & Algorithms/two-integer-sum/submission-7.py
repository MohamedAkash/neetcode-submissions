class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n^2) Brute force
        # space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                firstOccurance = target - nums[i]
                return [hashmap[firstOccurance], i]
            hashmap[nums[i]] = i
            