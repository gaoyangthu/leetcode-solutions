#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for l, element in enumerate(nums):
            try:
                r = nums.index(target - element, l + 1)
            except ValueError:
                continue
            else:
                return [l, r]
        raise ValueError('no solution')


def test():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print result
    nums = [0, 4, 3, 0]
    target = 0
    result = solution.twoSum(nums, target)
    print result

if __name__ == '__main__':
    test()
