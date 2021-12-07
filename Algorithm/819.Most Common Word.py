import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dictionary = {}
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^a-z\s]',' ',paragraph)
        for word in paragraph.split():
            try:
                dictionary[word] += 1
            except:
                dictionary[word] = 1
        count = -1
        most_freq = ""
        for k, v in dictionary.items():
            if v > count and k not in banned :
                most_freq = k
                count = v
        return most_freq