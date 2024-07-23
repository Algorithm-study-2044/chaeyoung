class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            if i == len(nums)-1:
                return False
            elif nums[i] in nums[i+1:]:
                return True
            else:
                continue

#왜안돼?
solution = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(solution.containsDuplicate(nums))
