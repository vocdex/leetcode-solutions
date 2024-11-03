# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        # Get length
        length,tail=1,head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        if k==0:
            return head
        # now rotate
        curr=head
        for i in range(length-k-1):
            curr=curr.next
        new_head=curr.next # new_head is the start of the split 2
        curr.next=None # original last element in split 1 points to None
        tail.next=head # original last element now points to original head
        return new_head
        
        