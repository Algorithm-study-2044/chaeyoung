class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def check_node(self, root, sum=0):
        #print(f"확인 중인 노드 값 : {root.val}, 현재까지의 합 :{sum}")
        if (root.val >= self.low) and (root.val <= self.high):
            sum += root.val
            #print(f"현재 노드 {root.val}은 범위 내에 존재함, 바뀐 합: {sum}")
        if root.left: sum = self.check_node(root.left, sum) #원래 여기서 sum = 안해줬더니 sum 이 지역변수가 되었음.. 왜지
        if root.right: sum = self.check_node(root.right, sum)
        return sum

    def rangeSumBST(self, root, low, high):
        self.low = low
        self.high = high
        return self.check_node(root)

