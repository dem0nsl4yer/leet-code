# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #defining current as head. 
        curr = head 

        while curr:
            b = curr.next # to keep saving ref. to curr.next 
            curr.next = prev
            prev = curr 
            curr = b
            #curr.next = prev # backpedaling - next to current will become prev. 
            #prev = curr # current node becomes previous 
            #curr = next_node # with both next and previous associations defined, current address is changed to next_node. 
        return prev  