class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        import heapq

        heap = []
        mat_onlysum = []
        result = []
        for i in range(len(mat)):
            n = sum(mat[i])
            heapq.heappush(heap, n)
            mat_onlysum.append(n)

        for j in range(k):
            lowest_num = heapq.heappop(heap)
            a = mat_onlysum.index(lowest_num)
            mat_onlysum[a] = -1
            result.append(a)

        return result


solution = Solution()


mat = [[1,1,0,0,0],
       [1,1,1,1,0],
       [1,0,0,0,0],
       [1,1,0,0,0],
       [1,1,1,1,1]]

k= 3

print(solution.kWeakestRows(mat,k))