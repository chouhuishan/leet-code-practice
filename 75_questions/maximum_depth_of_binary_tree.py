from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# SOLUTION 1 : Recursive DFS
class Solution:
    def maxDepth(self, root: list[TreeNode] | None) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# SOLUTION 2 : BFS
class Solution:
    def maxDepth(self, root: list[TreeNode] | None) -> int:
        if not root:
            return 0

        level = 0
        dq = deque()
        dq.append(root)

        while dq:
            for i in range(len(dq)):
                node = dq.popleft()

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            level += 1

        return level


# SOLUTION 3 : Iterative DFS
class Solution:
    def maxDepth(self, root: list[TreeNode] | None) -> int:
        if not root:
            return 0

        stack = []
        stack.append([root, 1])
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res


root = [3, 9, 20, None, None, 15, 7]
root = [1, None, 2]

print(Solution().maxDepth(root))
