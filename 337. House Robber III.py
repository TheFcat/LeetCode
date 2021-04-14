# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            node.left_child_dp = dfs(node.left)
            node.right_child_dp = dfs(node.right)
            left_grandchild_dp = 0 if not node.left else node.left.left_child_dp + node.left.right_child_dp
            right_grandchild_dp = 0 if not node.right else node.right.left_child_dp + node.right.right_child_dp
            return max(node.val + left_grandchild_dp + right_grandchild_dp, node.left_child_dp + node.right_child_dp)

        return dfs(root)
