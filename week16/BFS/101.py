# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def checking_symmetric(self, l, r):
        if not (l or r): # l, r이 모두 None일 때
            return True
        elif not (l and r): # l, r 중 하나만 존재할 때
            return False

        # l, r 이 모두 존재할 때
        if l.val == r.val:
            l_checker = self.checking_symmetric(l.left, r.right)
            r_checker = self.checking_symmetric(l.right, r.left)
            return bool(l_checker and r_checker)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checking_symmetric(root.left, root.right)
