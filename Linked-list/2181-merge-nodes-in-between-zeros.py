# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        temp = head.next
        temp1 = dummy_head
        sum_val = 0 

        while(temp):
            if temp.val == 0:
                if sum_val != 0:
                    temp1.next = ListNode(sum_val)
                    temp1 = temp1.next
                    sum_val = 0 
            else:
                sum_val += temp.val 
            temp = temp.next 

        return dummy_head.next 