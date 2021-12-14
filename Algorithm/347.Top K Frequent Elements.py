from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        top_k_frequent = Counter(nums).most_common(k)
        answers = [val for val, freq in top_k_frequent]
        return answers

