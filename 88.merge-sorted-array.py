#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        index = m + n - 1
        # set 3 pointers
        while index1 >= 0 and index2 >= 0:
            # put the bigger one to the last of list
            if nums1[index1] > nums2[index2]:
                nums1[index] = nums1[index1]
                index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index2 -= 1
            index -= 1
        nums1[: index2 + 1] = nums2[: index2 + 1]
        # if nums2 has ints left, they must be the smaller ones.
        """
        Do not return anything, modify nums1 in-place instead.
        """


# @lc code=end
