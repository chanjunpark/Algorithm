class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = []
        anagram = {}
        count = 0
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram.keys():
                word_dict.append([word])
                anagram[sorted_word] = count
                count += 1
            else:
                index = anagram.get(sorted_word)
                word_dict[index].append(word)
        return word_dict