# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root):
        def search(root, count):
            nonlocal ans
            if not root:
                return

            count[root.val] += 1
            if not root.left and not root.right:
                has_odd = 0
                for val in count.values():
                    if val % 2 == 1:
                        has_odd += 1
                if has_odd <= 1:
                    ans += 1

            search(root.left, count)
            search(root.right, count)
            count[root.val] -= 1

        count = dict()
        ans = 0
        search(root, count)

        return ans


