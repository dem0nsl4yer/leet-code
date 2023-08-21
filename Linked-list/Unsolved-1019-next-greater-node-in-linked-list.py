# Need to use stack as the output is supposed to be an integer list. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        dummy = ListNode(0)
        temp = dummy

        while(head and head.next):
            if head.val < head.next.val:
                temp.next = ListNode(head.next.val)
                temp = temp.next
            head = head.next
        return dummy.next