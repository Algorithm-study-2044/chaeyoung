class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        return False

solution = Solution()
s = "anagram"
t = "nagaram"

print(solution.isAnagram(s, t))


#문자열은 .sort()가 안된다. 신기? - 아 immutable이라 그런듯 + list의 메소드