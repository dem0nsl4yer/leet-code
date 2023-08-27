# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, sumt):
            if not node:
                return sumt
            right_sum = dfs(node.right, sumt)
            node.val += right_sum
            left_sum = dfs(node.left, node.val)
            return left_sum
        dfs(root, 0)
        return root
