# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while head:
            temp=head.next # temporarily store the next node
            head.next=prev # curr is now reversed null<-curr
            # next node:
            prev=head   # prev is now the current node 
            head=temp # move to the next node 
        return prev