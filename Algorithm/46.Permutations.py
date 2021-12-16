class Solution:

    def get_permutation(self, nums: list, count: int, stack: list):
        if count == 1:
            for num in nums:
                if num not in stack:
                    stack.append(num)
                    temp = stack.copy()
                    answer.append(temp)
                    stack.pop()

        else:
            for num in nums:
                if num not in stack:
                    stack.append(num)
                    self.get_permutation(nums, count - 1, stack)
                    stack.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:

        global stack
        global answer

        stack = []
        answer = []

        self.get_permutation(nums, len(nums), stack)

        return answer


