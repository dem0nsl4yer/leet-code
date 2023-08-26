## Basic solution 

# Iterates over whole tree and then compares leaves.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if not node:
                return 
            if not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.left,leaves)
            dfs(node.right,leaves)
        leaves1 = []
        dfs(root1, leaves1)
        leaves2 = []
        dfs(root2, leaves2)
        return leaves1 == leaves2


# Efficient solution - returns false as soon as there is a mismatch 
# DFS function needs to take both root1 and root2 as input. - did not work as it was matching across values - needs more work. 

# solution with direct comparison - well does **NOT** saves time - as it iterates, rather than direct string compare. 

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)
        
        leaves1 = get_leaves(root1)
        leaves2 = get_leaves(root2)
        
        if len(leaves1) != len(leaves2):
            return False
        
        for val1, val2 in zip(leaves1, leaves2):
            if val1 != val2:
                return False
        
        return True


## CLEAN solution - modular DFS an compare. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,l):
        if root==None:
            return
        if root.left==None and root.right==None:
            l.append(root.val)
            return
        self.dfs(root.left,l)
        self.dfs(root.right,l)
        


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1=[]
        l2=[]
        self.dfs(root1,l1)

        self.dfs(root2,l2)
        if l1==l2:
            return True
        return False