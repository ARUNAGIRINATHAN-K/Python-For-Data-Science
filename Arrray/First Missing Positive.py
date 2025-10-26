class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            # Put nums[i] in the correct index while it's in range and not already correct
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # After rearrangement, check which index is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
