class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        res = nums[0]

        if len(nums) == 1:
            return res

        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
                count = 1
            elif nums[i] == res:
                count += 1
            else:
                count -= 1
        return res


