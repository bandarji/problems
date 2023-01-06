class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        count = len(stack)
        return stack[count // 2]
