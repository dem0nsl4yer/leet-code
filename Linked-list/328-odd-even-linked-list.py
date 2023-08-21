# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Basically the idea is to swap out the odd and even values. 
        even = even_head = ListNode(None)
        odd = odd_head = ListNode(None)
        counter = 1 
        while(head):
            if counter %2 == 0:
                even.next = ListNode(head.val)
                even = even.next
            else:
                odd.next = ListNode(head.val)
                odd = odd.next 
            counter += 1
            head = head.next
        odd.next = even_head.next
        return odd_head.next