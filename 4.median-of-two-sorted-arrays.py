#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        left_Median_Index = (length1 + length2 + 1) // 2
        right_Median_Index = (length1 + length2 + 2) // 2

        def getKthSmallest(nums1, start1, end1, nums2, start2, end2, k):
            curLen1 = end1 - start1 + 1
            curLen2 = end2 - start2 + 1
            if curLen1 > curLen2:
                return getKthSmallest(nums2, start2, end2, nums1, start1, end1, k)
            if curLen1 == 0:
                return nums2[start2 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])

            idx1 = start1 + min(curLen1, k // 2) - 1
            idx2 = start2 + min(curLen2, k // 2) - 1

            if nums1[idx1] > nums2[idx2]:
                return getKthSmallest(
                    nums1, start1, end1, nums2, idx2 + 1, end2, k - (idx2 - start2 + 1)
                )
            else:
                return getKthSmallest(
                    nums1, idx1 + 1, end1, nums2, start2, end2, k - (idx1 - start1 + 1)
                )

        left_Median = getKthSmallest(
            nums1, 0, length1 - 1, nums2, 0, length2 - 1, left_Median_Index
        )
        right_Median = getKthSmallest(
            nums1, 0, length1 - 1, nums2, 0, length2 - 1, right_Median_Index
        )
        return (left_Median + right_Median) / 2


# @lc code=end
