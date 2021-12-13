class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        answer = [0 for x in temperatures]

        for idx, temperature in enumerate(temperatures):
            if idx == 0:
                stack.append([idx, temperature])
            else:

                while len(stack) > 0 and stack[-1][1] < temperature:
                    answer[stack[-1][0]] = idx - stack[-1][0]
                    stack.pop()
                stack.append([idx, temperature])

        return answer

