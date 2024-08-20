class Solution(object):
    def rules(self, tmpStr):
        if tmpStr[-1] == 'a':
            return ['e']
        elif tmpStr[-1] == 'e':
            return ['a', 'i']
        elif tmpStr[-1] == 'i':
            return ['a', 'e', 'o', 'u']
        elif tmpStr[-1] == 'o':
            return ['i', 'u']
        else:
            return ['a']


    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # a -> e
        # e -> a, i
        # i -> a, e, o, u
        # o -> i, u
        # u -> a
        vowels = ['a', 'e', 'i', 'o', 'u']
        results = ['a', 'e', 'i', 'o', 'u']
        if n == 0:
            return 0
        elif n == 1:
            return len(results)
        newResults = []
        for i in range(n - 1):
            for _ in range(len(results)):
                nextVs = self.rules(results[_])
                for w in nextVs:
                    newResults.append(results[_] + w)
            print(newResults)
            results = newResults
            newResults = []
        return len(results) % (10 ** 9 + 7)



solution = Solution()

solution.countVowelPermutation(3)