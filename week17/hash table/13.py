class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic_r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(s)):
            if i == len(s)-1 or dic_r2i[s[i]] >= dic_r2i[s[i+1]]:
                result += dic_r2i[s[i]]
                print(result)

            else:
                result -= dic_r2i[s[i]]
                print(result)

        return result

solution = Solution()
s="MCMXCIV"
print(solution.romanToInt(s))
