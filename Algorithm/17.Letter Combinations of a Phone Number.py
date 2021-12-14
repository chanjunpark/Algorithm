class Solution:

    def get_combinations(self, digits, stack):
        if len(digits) == 1:
            for char in digit_to_alpha.get(digits):
                temp = stack.copy()
                temp.append(char)
                temp = "".join(temp)
                answer.append(temp)

        else:
            for char in digit_to_alpha.get(digits[0]):
                stack.append(char)
                self.get_combinations(digits[1:], stack)
                stack.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        global digit_to_alpha
        global answer
        global stack

        digit_to_alpha = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                          "9": "wxyz"}
        answer = []
        stack = []

        if len(digits) >= 1:
            self.get_combinations(digits, stack)

        return answer
