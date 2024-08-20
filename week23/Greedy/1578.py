class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        colorsList = list(colors)
        memo = [0]
        result = 0

        for i in range(1, len(neededTime)):
            if colorsList[i-1] != colorsList[i]:
                memo.append(i)
                sameColorList = neededTime[memo[-2]:memo[-1]]
                if not len(sameColorList) == 1:
                    result += sum(sameColorList) - max(sameColorList)
            elif i == len(neededTime) - 1:
                memo.append(i+1)
                sameColorList = neededTime[memo[-2]:memo[-1]]
                if not len(sameColorList) == 1:
                    result += sum(sameColorList) - max(sameColorList)
        return result


solution = Solution()

#solution.minCost("aabaa", [1,2,3,4,1])
solution.minCost("abc", [1,2,3])