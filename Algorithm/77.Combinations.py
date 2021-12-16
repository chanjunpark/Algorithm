class Solution:

    def get_combination(self, n_list: list, k: int, stack: list):
        if k == 1:
            for j in n_list:
                stack.append(j)
                temp = stack.copy()
                answer.append(temp)
                stack.pop()
        else:
            for idx in range(len(n_list)):
                stack.append(n_list[idx])
                self.get_combination(n_list[idx + 1:], k - 1, stack)
                stack.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:

        global stack
        global answer

        stack = []
        answer = []
        n_list = [integer for integer in range(1, n + 1)]

        self.get_combination(n_list, k, stack)

        return answer
