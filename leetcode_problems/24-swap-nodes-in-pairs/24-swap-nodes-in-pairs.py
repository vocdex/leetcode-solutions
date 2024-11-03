# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head) # points to head: dummy->head
        curr=dummy  # current node is dummy
        while curr.next and curr.next.next:
            first_node=curr.next # first node in pair
            second_node=curr.next.next # second node in pair
            first_node.next=second_node.next # swapping first node pointer to second node pointer 
            curr.next=second_node # second node in pair (not swapped yet)
            curr.next.next=first_node # dummy now points to the start of the next pair
            curr=curr.next.next # update curr
        return dummy.next