class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # not i+1 because we can reuse same element
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return res
