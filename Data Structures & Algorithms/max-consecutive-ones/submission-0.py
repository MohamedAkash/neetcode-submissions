class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNumber = 0
        ConsecutiveOnes = 0
        for num in nums:
            if num == 1:
                ConsecutiveOnes += 1
            else:
                ConsecutiveOnes = 0
            maxNumber = max(maxNumber, ConsecutiveOnes)
        return maxNumber
    