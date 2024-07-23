class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in nums[i+1:]:
                nums[i] = ""
                return [i, nums.index(num_to_find)]
