class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = q = head 
        while p.next:
            if p.next.next:
                p = p.next.next
            else:
                p = p.next
            q = q.next
        return q 
