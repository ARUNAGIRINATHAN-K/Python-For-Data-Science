class Solution:
    def searchRange(self, nums, target):
        def find_first():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1  # keep looking on the left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        def find_last():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1  # keep looking on the right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        return [find_first(), find_last()]
