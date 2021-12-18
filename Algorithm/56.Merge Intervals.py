class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        stack = []

        for pair in sorted(intervals, key=lambda x: (x[0], x[1])):
            if len(stack) == 0:
                stack.append(pair)
            else:
                if pair[0] <= stack[-1][1]:
                    merge = [stack[-1][0], max(stack[-1][1], pair[1])]
                    stack.pop()
                    stack.append(merge)
                else:
                    stack.append(pair)

        return stack
