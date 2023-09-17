## Not working 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return 
        st_f = st = []

        counter = 0 
        if root:
            counter += root.val
            st.append(root.val)
            if counter == targetSum:
                st_f.append(st)
        if root.left:
            left_val = self.pathSum(root.left, targetSum)
        if root.right:
            right_val = self.pathSum(root.right, targetSum)

        return st_f


## - standard DFS approach. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, current_sum):
            if not node:
                return 
            path.append(node.val)
            current_sum += node.val
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path[:]) # - creating a copy of the path stack - so this does not affects the list bein popped
                                       # on backtracking later. 

            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)

            ## Key part - backtracking the last node when moving up a tree
            path.pop()

        result = []
        dfs(root, [], 0)
        return result 