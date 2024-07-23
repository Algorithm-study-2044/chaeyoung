# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.max = 0

    def diameter_checker(self, root):
        if not root:
            return 0

        l = self.diameter_checker(root.left)
        r = self.diameter_checker(root.right)
        current_max = l + r
        self.max = max(self.max, current_max)
        return max(l+1, r+1)


    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter_checker(root)
        return self.max
