class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            count =0
            for j in range(n):
                if nums[j]< nums[i]:
                    count +=1
            ans.append(count)
        return ans



        