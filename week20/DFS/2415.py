# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reversewithN(self, l, r, n):

        if n % 2 == 1:
            l.val, r.val = r.val, l.val

        if l.left:
            n += 1
            self.reversewithN(l.left, r.right, n)
            self.reversewithN(l.right, r.left, n)
        return


    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        n = 1
        if root.left:
            self.reversewithN(root.left, root.right, n)

        return root
