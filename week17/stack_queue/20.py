class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_stack = []
        opening_p = ['(', '{', '[']
        closing_p = [')', '}', ']']

        if s[0] in closing_p:
            return False

        for _ in s:
            if _ in opening_p:
                temp_stack.append(_)
            else:
                i = closing_p.index(_)
                if temp_stack and temp_stack.pop() == opening_p[i]:
                    continue
                else:
                    return False


        return False if temp_stack else True
