class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        temp = [1, 1]
        result = []

        for i in range(1, numRows + 1):
            if i == 1:
                result.append([1])
                continue
            elif i == 2:
                result.append([1, 1])
                continue
            prev = temp
            temp = [0] * i
            for j in range(i):
                if j == 0 or j == i - 1:
                    temp[j] = 1
                    continue
                temp[j] = prev[j - 1] + prev[j]
            result.append(temp)

        return result

