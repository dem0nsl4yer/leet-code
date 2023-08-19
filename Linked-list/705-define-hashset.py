# need to implement the remove function. 

class MyHashSet:

    def __init__(self):
        self.head = None
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            new_node = ListNode(key)
            new_node.next = self.head
            self.head = new_node 
            
    def remove(self, key: int) -> None:
        if self.contains(key):
            temp = self.head
            prev = temp
            if key == temp.next.val:
                temp.next = temp.next.next 
            


    def contains(self, key: int) -> bool:
        temp = self.head
        while temp:
            if key == temp.val:
                return True 
            temp = temp.next
        return False 

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)