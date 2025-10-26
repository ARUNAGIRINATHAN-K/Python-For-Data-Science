class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort to manage duplicates
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates on the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
