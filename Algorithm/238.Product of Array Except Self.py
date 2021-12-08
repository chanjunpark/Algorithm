class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side = []
        right_side = []
        answer = []

        for index in range(len(nums)):
            if index == 0:
                left_side.append(nums[index])
                right_side.append(nums[-index - 1])
            else:
                left_side.append(left_side[index - 1] * nums[index])
                right_side.append(right_side[index - 1] * nums[-index - 1])

        for x in range(len(nums)):
            if x == 0:
                answer.append(right_side[-x - 2])
            elif x == len(nums) - 1:
                answer.append(left_side[x - 1])
            else:
                answer.append(left_side[x - 1] * right_side[-x - 2])

        return answer
