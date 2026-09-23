class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums ==[]:
            return 0
        nums.sort()
        count =1
        longest =1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                count +=1
            elif nums[i] == nums[i-1]:
                continue
            else:
                count =1
            
            longest=max(longest, count)
        return longest

        