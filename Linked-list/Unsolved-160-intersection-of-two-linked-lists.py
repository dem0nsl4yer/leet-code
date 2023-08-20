# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tmpA = headA
        tmpB = headB
        counter = 0 
        while (tmpA.next and tmpB.next):
            combo = False 
            if tmpA.val == tmpB.val and tmpA.next.val == tmpB.next.val:
                combo = True
            else:
                combo = False
            if combo == False:                
                counter += 1
            tmpA = tmpA.next
            tmpB = tmpB.next
        return counter 