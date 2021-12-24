class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for num in nums:
            subsets = answer.copy()
            for subset in subsets:
                temp = subset.copy()
                temp.append(num)
                answer.append(temp)

        return answer
