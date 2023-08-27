# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Store data in an array path, and just concatenate it when we encounter leaf node. 
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            if not node:
                return []
            path.append(str(node.val))

            if not node.left and not node.right:
                return ['->'.join(path)]
            return dfs(node.left, path.copy()) + dfs(node.right, path.copy())
        return dfs(root, [])