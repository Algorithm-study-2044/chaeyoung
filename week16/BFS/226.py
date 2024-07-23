# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def tree_inverter(self, root):
        if not root:
            return None
        left = root.left
        right = root.right
        root.left = self.tree_inverter(right)
        root.right = self.tree_inverter(left)
        return root

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.tree_inverter(root)

