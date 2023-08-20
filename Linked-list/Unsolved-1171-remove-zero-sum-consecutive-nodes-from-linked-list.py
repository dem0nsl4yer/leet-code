# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head 
        while(temp.next and temp.next.next):
            if temp.next.val + temp.next.next.val == 0:
                temp.next = temp.next.next.next
            prev = temp
            temp = temp.next 
        return head