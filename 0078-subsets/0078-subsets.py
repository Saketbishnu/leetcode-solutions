class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(pos, res, path):
            for i in range(pos, len(nums)):
                path.append(nums[i])
                dfs(i + 1, res, path)
                path.pop()
            res.append([i for i in path])
        dfs(0, res, [])
        return res
        