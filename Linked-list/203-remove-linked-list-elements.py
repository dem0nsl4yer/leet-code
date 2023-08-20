# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
# Adding dummy to handle the first element. 
        dummy_head = ListNode(0)
        dummy_head.next = head 
        tmp = dummy_head 
        if head is None:
            return None 
        while tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next 
        return dummy_head.next 