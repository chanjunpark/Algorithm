from itertools import combinations


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid_tripets = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tripet = [nums[i], nums[left], nums[right]]
                if sum(tripet) == 0 and tripet not in valid_tripets:
                    valid_tripets.append(tripet)
                    left += 1
                    right -= 1
                elif sum(tripet) < 0:
                    left += 1
                else:
                    right -= 1

        return valid_tripets

