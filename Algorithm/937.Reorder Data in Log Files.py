class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []
        for x in logs:
            if x.split(" ")[1].isalpha():
                letter_log.append(x)
            else:
                digit_log.append(x)

        letter_log = sorted(letter_log, key=lambda x: (x.split(" ")[1:], x.split()[0]))

        return letter_log + digit_log
