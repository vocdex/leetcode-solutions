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
        # dummy is the node that points to head
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        while curr and curr.next:
            nextPairstart=curr.next.next # starting point for the next pair
            second=curr.next # declaring the second node in swapping pair
            # reverse this pair
            second.next=curr
            curr.next=nextPairstart
            prev.next=second # changing the prev point to the original second node which is now the #first node in the new pair
            #update pointers
            prev=curr # this node now points to the node before the starting node of the next pair
            curr=nextPairstart # curr is the starting node of the next pair
        return dummy.next
            
            