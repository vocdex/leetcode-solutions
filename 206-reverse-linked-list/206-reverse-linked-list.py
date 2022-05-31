# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        stack=ListNode(head.val)
        head=head.next
        while head is not None:
            temp=ListNode(head.val)
            temp.next=stack
            stack=temp
            head=head.next
        return stack
