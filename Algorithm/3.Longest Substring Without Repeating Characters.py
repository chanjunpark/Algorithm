class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_string = ""
        length = []

        if not s:
            return 0
        else:
            for c in s:
                if c not in longest_string:
                    longest_string += c
                else:
                    length.append(len(longest_string))
                    for pt in range(len(longest_string)):
                        if longest_string[pt] == c:
                            longest_string = longest_string[pt + 1:] + c
                            break
            length.append(len(longest_string))
            return max(length)
