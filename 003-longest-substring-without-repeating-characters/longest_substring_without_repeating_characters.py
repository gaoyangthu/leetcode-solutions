#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        max_len = 0
        head = 0
        i = 0
        while i < l:
            j = s[head:i].find(s[i])
            if j > -1:
                max_len = max(max_len, i - head)
                head = head + j + 1
            i += 1
        return max(max_len, i - head)


def test():
    solution = Solution()
    s = 'abcabcbb'
    print solution.lengthOfLongestSubstring(s)
    s = 'bbbbb'
    print solution.lengthOfLongestSubstring(s)
    s = 'pwwkew'
    print solution.lengthOfLongestSubstring(s)
    s = 'ab'
    print solution.lengthOfLongestSubstring(s)
    s = 'a'
    print solution.lengthOfLongestSubstring(s)
    s = ''
    print solution.lengthOfLongestSubstring(s)

if __name__ == '__main__':
    test()
