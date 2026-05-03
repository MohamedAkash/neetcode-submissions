class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left1, left2 = m - 1, n - 1
        tail = len(nums1) - 1
        while left1 >= 0 or left2 >= 0:
            if left1 < 0 or (left2 >= 0 and nums1[left1] < nums2[left2]):
                nums1[tail] = nums2[left2]
                left2 -= 1
            else:
                nums1[tail] = nums1[left1]
                left1 -= 1
            tail -= 1
        return nums1
