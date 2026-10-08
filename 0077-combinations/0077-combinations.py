class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start, current):
            # We have selected k numbers
            if len(current) == k:
                result.append(current.copy())
                return

            for i in range(start, n + 1):
                current.append(i)

                backtrack(i + 1, current)

                current.pop()

        backtrack(1, [])

        return result