# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        c = root.val
    # Trick - root value is the smallest, as chilren are >= root. 
        def dfs(node, b):
            if not node:
                return float('inf')
            if node.val < b and node.val > c:
                b = node.val
            if not node.left:
            # because this tree either has 0 sub-nodes or 2. 
                return b
            return min(dfs(node.left, b) , dfs(node.right, b))
        d = dfs(root, float('inf')) 
        return d if d != float('inf') else -1