# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth ==1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root


        def dfs( node, val, depth, current_depth):
            if not node:
                return 
        
            if current_depth == depth-1:
                left_child = TreeNode(val)
                left_child.left = node.left
                node.left = left_child

                right_child = TreeNode(val)
                right_child.right = node.right
                node.right = right_child
            else:
                dfs(node.left, val, depth, current_depth+1)
                dfs(node.right, val, depth, current_depth+1)

        dfs(root, val, depth, current_depth=1)
        return root
    
##  No dfs: 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        dummy.next = root
        counter = 0 
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        if depth == 2:
            k_left = TreeNode(val)
            k_left.left = root.left
            root.left = k_left


            k_right = TreeNode(val)
            k_right.right = root.right
            root.right = k_right

        if root.left:
            left_depth = self.addOneRow(root.left, val, depth-1)
        if root.right:
            right_depth = self.addOneRow(root.right, val, depth-1)
        return dummy.next 