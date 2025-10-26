class Solution:
    def permute(self, nums):
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])  # make a copy
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return res
