class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, val in enumerate(nums):
            num2find = target - val

            if num2find in seen:
                return [seen[num2find], idx]
            else:
                seen[val] = idx
