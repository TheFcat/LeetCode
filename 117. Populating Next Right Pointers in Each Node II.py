
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def link(node, back=None):
            if not node:
                if back:
                    back.next = None
                return
            if node.left:
                if back:
                    back.next = node.left
                if node.right:
                    node.left.next = node.right
                    back = node.right
                else:
                    back = node.left
            elif node.right:
                if back:
                    back.next = node.right
                back = node.right

            link(node.next, back)

        def find_next_start(node):
            if not node:
                return
            if node.left:
                start = node.left
            elif node.right:
                start = node.right
            else:
                start = find_next_start(node.next)
            return start

        def link_all(node):
            if not node:
                return
            link(node)
            start = find_next_start(node)
            link_all(start)

        link_all(root)

        return root




