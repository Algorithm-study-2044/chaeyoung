class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        left, right = 1, x

        while left <= right:
            mid = (left+right)//2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1

        return right

solution = Solution()
print(solution.mySqrt(8))