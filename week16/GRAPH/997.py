class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        trusted_list = [0] * (n+1)
        trust_list = [0] * (n+1)

        for i in range(len(trust)):
            trust_list[trust[i][0]] += 1
            trusted_list[trust[i][1]] += 1

        for i in range(1,n+1):
            if trust_list[i] == 0 and trusted_list[i] == n-1:
                return i

        return -1
