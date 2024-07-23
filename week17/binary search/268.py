class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l <= r:
            print(l, r)
            m = (l+r)//2
            if m < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l

solution = Solution()
nums = [9,6,4,2,3,5,7,0,1]
#nums = [0, 1]
print(solution.missingNumber(nums))
