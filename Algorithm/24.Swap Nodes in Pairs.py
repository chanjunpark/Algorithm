# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        root = answer
        answer.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            root.next = b

            head = head.next
            root = root.next.next

        return answer.next
