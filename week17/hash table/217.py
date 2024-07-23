class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        nums_set = set(nums)
        nums_set_list = sorted(list(nums_set)) #nums_set_list = list(nums_set).sort()는 왜 안될까

        if nums_set_list != nums:
            return True
        else:
            return False


solution = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(solution.containsDuplicate(nums))
