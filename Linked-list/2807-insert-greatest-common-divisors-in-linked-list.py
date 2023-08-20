# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gcd(num1, num2):
    x = min(num1, num2)
    counter = 1
    for i in range(1, x+1):
        if num1%i == 0 and num2%i == 0:
            counter = i
    return counter 

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while tmp.next:
            k = gcd(tmp.val, tmp.next.val)
            m = ListNode(k)
            m.next = tmp.next
            tmp.next = m 
            tmp = tmp.next.next
        return head 