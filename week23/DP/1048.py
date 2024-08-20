class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        ans = dict()

        for word in words:
            print(word)
            ans[word] = 1
            for pos in range(len(word)):
                smaller = word[:pos] + word[pos + 1:]
                if smaller in words:
                    ans[word] = max(ans[word], ans[smaller] + 1)

        return max(ans.values())

