# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


class Solution(object):
    def flatten(self, root):
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
