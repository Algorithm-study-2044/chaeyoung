class Solution(object):
    def backspace_processing(self, sent):
        sent_stack = []
        for _ in sent:
            print(_)
            if _ == '#':
                if sent_stack:
                    sent_stack.pop()
            else:
                sent_stack.append(_)

        return sent_stack

    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_stack = self.backspace_processing(s)
        t_stack = self.backspace_processing(t)

        return True if s_stack == t_stack else False


solution = Solution()
print(solution.backspaceCompare("아##씨", "#아#씨"))