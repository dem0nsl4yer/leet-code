# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ctr):
            if not node:
                return 0
            ctr += 1
            if not node.left and not node.right:
                return ctr
            if node.left and node.right:
                return min(dfs(node.left, ctr), dfs(node.right, ctr))
            elif node.left:
                return dfs(node.left,ctr)
            else:
                return dfs(node.right,ctr)
        return dfs(root, 0)
    
### somehow more time taking solution - more elegant. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ctr):
            if not node:
                return float('inf')
            ctr += 1
            if not node.left and not node.right:
                return ctr
            return min(dfs(node.left, ctr), dfs(node.right, ctr))
        if not root:
            return 0
        return dfs(root, 0)