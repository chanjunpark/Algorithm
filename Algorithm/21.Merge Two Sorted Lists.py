# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def compare_two_number(self, a, b):
        if a > b:
            return a
        else:
            return b

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        answer = ListNode()
        current = answer

        while list1 and list2:
            if list1.val < list2.val:
                new_node = ListNode(val=list1.val)
                current.next = list1
                list1 = list1.next
            else:
                new_node = ListNode(val=list2.val)
                current.next = list2
                list2 = list2.next
            current = current.next
        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next
        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next
        answer = answer.next

        return answer
