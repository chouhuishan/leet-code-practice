# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> bool:
        
        def dfs(root : TreeNode | None, leaf: list[int]) -> None:
            if not root:
                return 
            
            if not root.left and not root.right: # if root.left and root.right is None = node exist with 0 children
                leaf.append(root.val)
                return 
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        if leaf1 == leaf2:
            return True


root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
# root1 = [1, 2, 3]
# root2 = [1, 3, 2]
print(Solution().leafSimilar(root1, root2))
