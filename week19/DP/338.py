class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            a = sum(map(int, list(str(bin(i + 1))[2:])))
            result.append(a)

        return result