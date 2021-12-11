class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        is_first = True
        for idx, char in enumerate(s):
            if is_first:
                stack.append(char)
                is_first = False
            else:
                if char <= stack[-1] and char not in stack:
                    while len(stack) > 0 and char <= stack[-1] and stack[-1] in s[idx + 1:]:
                        stack.pop()
                    stack.append(char)
                else:
                    if char not in stack:
                        stack.append(char)

        return "".join(stack)
