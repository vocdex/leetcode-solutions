# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        prev,curr=None,head
        i=0
        while curr and i<left-1:
            prev=curr
            curr=curr.next
            i+=1
        last_node_1=prev
        last_node_sublist=curr
        temp=None
        i=0
        while curr and i<right-left+1:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            i+=1
        if last_node_1:
            last_node_1.next=prev
        else:
            head=prev
        last_node_sublist.next=curr
        return head