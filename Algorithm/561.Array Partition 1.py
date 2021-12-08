class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maximum = 0

        while len(nums) > 0:
            nums.pop()
            maximum += nums.pop()

        return maximum
