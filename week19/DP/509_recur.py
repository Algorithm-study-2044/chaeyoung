class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return 1
        return self.fib(n-2) + self.fib(n-1)