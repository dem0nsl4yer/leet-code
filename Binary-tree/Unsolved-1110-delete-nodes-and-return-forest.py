# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, parent, is_root):
            if not node:
                return None
            
            if node.val in to_delete:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
 
                if node.left and node.left.val not in to_delete:
# problem is adding a sub-tree here which may have nodes that require deletion.
                    forest.append(node.left)
                if node.right and node.right.val not in to_delete:
# problem is adding a sub-tree here which may have nodes that require deletion.
                    forest.append(node.right)

                to_delete.remove(node.val)
                node = None            
            if is_root and node:
                forest.append(node)
            if node and node.left:
                dfs(node.left, node, node is None)
            if node and node.right:
                dfs(node.right, node, node is None)
        
        forest = []
        dfs(root, None, True)
        return forest






