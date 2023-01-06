from typing import Optional


TESTS = [
    ([1, 2, 2, 1], True),
    ([1, 2], False),
]


class ListNode:

    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values == values[::-1]
