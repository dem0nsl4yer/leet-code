class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums 
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.array[left:right+1])