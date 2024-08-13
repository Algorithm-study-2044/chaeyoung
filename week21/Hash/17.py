class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        charDict = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}
        if not digits:
            return []
        else:
            before = list(charDict[digits[0]])

        i = 1
        while i < len(digits):
            after = []
            for b in before:
                for alpha in charDict[digits[i]]:
                    after.append(b+alpha)
            before = after
            i += 1


        return before

solution = Solution()

print(solution.letterCombinations("2"))