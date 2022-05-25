# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        while curr and curr.next:
            # save ptrs
            nextPairStart=curr.next.next
            second=curr.next
            # reverse this pair
            second.next=curr
            curr.next=nextPairStart
            prev.next=second
            
            #update ptrs
            prev=curr
            curr=nextPairStart
        return dummy.next
        