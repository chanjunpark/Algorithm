class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        is_first = True

        for bracket in s:
            if is_first:
                stack.append(bracket)
                is_first = False
            else:
                if len(stack) == 0:
                    stack.append(bracket)
                else:
                    if ord(bracket) - ord(stack[-1]) <= 2 and ord(bracket) - ord(stack[-1]) > 0:
                        stack.pop()
                    else:
                        stack.append(bracket)

        return len(stack) == 0

