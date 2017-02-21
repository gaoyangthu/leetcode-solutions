#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def find_kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        m = nums1[k / 2 - 1] if len(nums1) >= k / 2 else None
        n = nums2[k / 2 - 1] if len(nums2) >= k / 2 else None
        if n is None or (m is not None and m < n):
            return self.find_kth(nums1[k / 2:], nums2, k - k / 2)
        else:
            return self.find_kth(nums1, nums2[k / 2:], k - k / 2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.find_kth(nums1, nums2, l / 2 + 1)
        else:
            return (self.find_kth(nums1, nums2, l / 2) + self.find_kth(nums1, nums2, l / 2 + 1)) / 2.0


def test():
    solution = Solution()
    print solution.findMedianSortedArrays([1, 2], [1, 2, 3])
    print solution.findMedianSortedArrays([1, 2], [1, 2])
    print solution.findMedianSortedArrays([1, 2], [3])
    print solution.findMedianSortedArrays([1], [2, 3])
    print solution.findMedianSortedArrays([4], [1, 2, 3, 5, 6])
    print solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 6])

if __name__ == '__main__':
    test()
