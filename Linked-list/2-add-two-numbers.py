# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        b = dummy 
        b.next = l1 
        copy = l1
        res = 0 
        while (l1 or l2):
            k1 = l1.val if l1 else 0 
            k2 = l2.val if l2 else 0 
            t = (k1 + k2+ res)%10 
            b.next = ListNode(t)
            res = (k1 + k2 + res)//10 
            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next
            b = b.next 
 
        if res > 0:  # Check if there's still a carry
            b.next = ListNode(res)      
        return dummy.next
