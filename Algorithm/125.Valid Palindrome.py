import re
import collections

class Solution:
    def isPalindrome_deque(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s.lower():
            if char.isalnum():
                strs.append(char)

        while len(strs) > 1 :
            if strs.popleft() != strs.pop():
                return False
        return True

    def isPalindrome_regexp(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        return s == s[::-1]


s = "A man, a plan, a canal: Panama"
solution = Solution()
if(solution.isPalindrome_deque(s)):
    print("True")
else:
    print("False")