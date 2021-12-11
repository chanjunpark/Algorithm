# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        reverse_list = ListNode()
        reverse = reverse_list.next

        new_list = ListNode();
        new = new_list

        index = 1

        while index <= right:
            if index >= left and index <= right:
                post = head.next
                head.next = reverse
                reverse = head
                head = post
                index += 1
            else:
                post = head.next
                head.next = None
                new.next = head
                new = new.next
                head = post
                index += 1
        new.next = reverse
        while new.next:
            new = new.next
        new.next = head
        new_list = new_list.next

        return new_list

