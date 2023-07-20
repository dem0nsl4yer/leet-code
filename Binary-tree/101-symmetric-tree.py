# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l= root.left
        r = root.right 
        def checksymmetry(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.val == right.val) and checksymmetry(left.right, right.left) and checksymmetry(right.right, left.left)
        return checksymmetry(l, r)