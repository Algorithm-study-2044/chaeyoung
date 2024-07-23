class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq

        heap = []

        for n in nums:
            heapq.heappush(heap, -n)

        m1 = -heapq.heappop(heap) - 1
        m2 = -heapq.heappop(heap) - 1

        return m1 * m2


solution = Solution()


nums= [3, 4, 5, 2]


print(solution.maxProduct(nums))