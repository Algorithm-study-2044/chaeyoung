class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        s = list(s)

        while s:
            cnt_l = 0
            cnt_r = 0
            while s:
                if s.pop(0) == 'L':
                    cnt_l += 1
                else:
                    cnt_r += 1
                if cnt_l == cnt_r:
                    cnt += 1
                    break
        return cnt