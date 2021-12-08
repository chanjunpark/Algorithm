# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        stack = collections.deque()

        while head:
            stack.append(head.val)
            head = head.next

        while len(stack) > 1:
            if stack.popleft() != stack.pop():
                return False
        return True
