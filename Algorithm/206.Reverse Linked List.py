# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        current = answer.next

        while head:
            post = head.next
            head.next = current
            current = head
            head = post

        return current
