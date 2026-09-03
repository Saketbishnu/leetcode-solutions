class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, current):
            # Base case: valid combination found
            if remaining == 0:
                result.append(current.copy())
                return

            # Try candidates starting from 'start'
            for i in range(start, len(candidates)):
                num = candidates[i]

                # Skip if number is larger than remaining target
                if num > remaining:
                    continue

                # Choose
                current.append(num)

                # Explore
                # i is passed again because the same number can be reused
                backtrack(i, remaining - num, current)

                # Unchoose (backtrack)
                current.pop()

        backtrack(0, target, [])
        return result