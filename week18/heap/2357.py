class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq

        cnt = 0


        while sum(nums):
            cnt += 1

            heap = []
            for n in nums:
                if n:
                    heapq.heappush(heap, n)

            x = heapq.heappop(heap)
            print(x)
            for i in range(len(nums)):
                if nums[i] > x:
                    nums[i] -= x
                else:
                    nums[i] = 0
            print(nums)
        return cnt


solution = Solution()
nums= [1, 2, 3, 5]

print(solution.minimumOperations(nums))