#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given two linked lists representing two non-negative numbers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = '(%s' % str(self.val)
        while self.next:
            self = self.next
            s += ' -> %s' % str(self.val)
        s += ')'
        return s


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        l = l1
        r = l2
        curr = result
        carry = 0
        while l is not None or r is not None:
            x = l.val if l else 0
            y = r.val if r else 0
            digit = carry + x + y
            carry = digit / 10
            curr.next = ListNode(digit % 10)
            curr = curr.next
            l = l.next if l else None
            r = r.next if r else None
        if carry > 0:
            curr.next = ListNode(carry)
        return result.next


def test():
    l1 = ListNode(2)
    curr = l1
    curr.next = ListNode(4)
    curr = curr.next
    curr.next = ListNode(3)
    l2 = ListNode(5)
    curr = l2
    curr.next = ListNode(6)
    curr = curr.next
    curr.next = ListNode(4)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print l1, l2, result
    l1 = ListNode(9)
    curr = l1
    curr.next = ListNode(9)
    l2 = ListNode(1)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print l1, l2, result

if __name__ == '__main__':
    test()
