# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p, q):
        self.ans = None
        def dfs(node):
            if self.ans is not None:
                return True

            if node is None:
                return False

            if node.val == p or node.val == q:
                return True
            left_result = dfs(node.left)
            right_result = dfs(node.right)

            if left_result is True and right_result is True:
                self.ans = node.val
                return True

            return bool(left_result or right_result)

        dfs(root)
        return self.ans

print(Solution().lowestCommonAncestor(TreeNode(3, TreeNode(1), TreeNode(5)),1, 5))