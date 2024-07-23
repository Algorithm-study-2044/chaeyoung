# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def num_of_node(self, root, n_dic):
        try:
            n_dic[root.val] += 1
        except KeyError:
            n_dic[root.val] = 1
        if root.left: n_dic = self.num_of_node(root.left, n_dic)
        if root.right: n_dic = self.num_of_node(root.right, n_dic)
        return n_dic

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """';kj'
        n_dic = dict()
        n_dic = self.num_of_node(root, n_dic)
        m_num = max(n_dic.values())
        result = []
        for _ in n_dic.keys():
            if n_dic[_] == m_num:
                result.append(_)
        return result








