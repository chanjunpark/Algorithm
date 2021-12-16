class Solution:

    def get_combination_sum(self, candidates, target, stack, sums):
        for num in candidates:
            stack.append(num)
            if sum(stack) == target:
                if sorted(stack) not in answer:
                    stack.sort()
                    temp = stack.copy()
                    answer.append(temp)
            elif sum(stack) < target:
                self.get_combination_sum(candidates, target, stack, sum(stack))
            else:
                stack.pop()
                break
            stack.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global stack
        global answer

        stack = []
        answer = []

        self.get_combination_sum(sorted(candidates), target, stack, 0)

        return answer