# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_node = ListNode()
        odd_list = odd_node

        even_node = ListNode()
        even_list = even_node

        while head and head.next:
            current = head
            post = head.next
            head.next = post.next
            head = head.next

            current.next = None
            odd_list.next = current
            odd_list = odd_list.next

            post.next = None
            even_list.next = post
            even_list = even_list.next

        if head:
            odd_list.next = head
            odd_list = odd_list.next

        odd_list.next = even_node.next

        return odd_node.next
