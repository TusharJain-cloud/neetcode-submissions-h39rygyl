# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursion
        # if head is None or head.next is None:
        #     return head
        
        # new_head = self.reverseList(head.next)

        # head.next.next = head
        # head.next = None

        # return new_head
        first, second = None, head

        while second:
            third = second.next
            second.next = first
            first = second
            second = third
        
        return first

        