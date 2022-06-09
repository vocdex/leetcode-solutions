# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=dummy
        while curr.next and curr.next.next:
            first_node=curr.next
            second_node=curr.next.next
            first_node.next=second_node.next
            curr.next=second_node
            curr.next.next=first_node
            curr=curr.next.next
        return dummy.next