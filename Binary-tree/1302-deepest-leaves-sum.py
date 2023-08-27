# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        summ = 0 
        lmax = 0 
        def dfs(node, loc):
            nonlocal lmax, summ
            if not node:
                return 0
            loc += 1
            if lmax <loc:
                summ = 0 
            lmax = max(loc, lmax)
            if not node.left and not node.right:
                if loc == lmax:
                    summ += node.val
            dfs(node.left, loc)  
            dfs(node.right,loc)
        dfs(root, 0)
        return summ