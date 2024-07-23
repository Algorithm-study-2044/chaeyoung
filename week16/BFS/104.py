# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def finding_depth(self, root, d):
        if root:
            d += 1
            return max(self.finding_depth(root.left, d), self.finding_depth(root.right, d))
        else:
            return d

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.finding_depth(root, 0)
