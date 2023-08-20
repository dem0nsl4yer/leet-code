class MyHashMap:

    def __init__(self):
        self.head = ListNode(-1) 
        

    def put(self, key: int, value: int) -> None:
        temp = self.head
        for i in range(key):
            if temp.next is None:
                temp.next = ListNode(-1)
            temp = temp.next
        temp.val = value
        

    def get(self, key: int) -> int:
        temp = self.head
        for i in range(key):
            if temp.next is None:
                return -1 
            temp = temp.next
        return temp.val 



    def remove(self, key: int) -> None:
        temp = self.head
        if self.get(key) != -1:
            for i in range(key - 1):  # Use key - 1 to access the node before key
                temp = temp.next
            temp.next = temp.next.next
        
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)