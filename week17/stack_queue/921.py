class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_stack = []

        for _ in s:
            print(f"처리중 : {s_stack}, 넣을 괄호: {_}")
            if not s_stack:
                s_stack.append(_)
            elif _ == ')' and s_stack[-1] == '(':
                s_stack.pop()
            else:
                s_stack.append(_)
            print(f"처리완료 : {s_stack}")

        return len(s_stack)

solution = Solution()
#dd
s = "))()()((("


print(solution.minAddToMakeValid(s))


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_stack = []

        for _ in s:
            if not s_stack:
                s_stack.append(_)
            elif _ == ')' and s_stack[-1] == '(':
                s_stack.pop()
            else:
                s_stack.append(_)

        return len(s_stack)