class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        import heapq

        num_list = []
        for _ in str(num):
            num_list.append(int(_))

        heapq.heapify(num_list)
        a = heapq.heappop(num_list)
        b = heapq.heappop(num_list)

        result = (a + b) * 10 + sum(num_list)

        if a < 2:
            result = min(result, a * 100 + b * 10 + sum(num_list))

        return result


