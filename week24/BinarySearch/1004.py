class Solution:
    def longestOnes(self, nums, k):
        left = 0
        answer = 0
        counts = {0: 0, 1: 0}

        for right, num in enumerate(nums):
            counts[num] += 1

            while counts[0] > k:
                counts[nums[left]] -= 1
                left += 1

            curr_window_size = right - left + 1
            answer = max(answer, curr_window_size)

        return answer