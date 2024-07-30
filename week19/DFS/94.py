# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.result = []
    def inordert(self, n):
        if n:
            self.inordert(n.left)
            self.result.append(n.val)
            self.inordert(n.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inordert(root)
        return self.result

