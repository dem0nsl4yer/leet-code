
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        counter = 1
        node1 = None  # Initialize node1
        val1 = None   # Initialize val1
        
        while temp:
            if counter == k:
                node1 = temp
                val1 = temp.val 
            temp = temp.next 
            counter += 1 
        
        # Reinitialize temp and counter
        temp = head
        count = 1
        while temp:
            if count == counter - k:  # Should be "counter == k" instead of "counter == counter - k"
                node1.val, temp.val = temp.val, node1.val
            temp = temp.next 
            count += 1 
            
        return head 
