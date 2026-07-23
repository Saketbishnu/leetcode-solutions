class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq= {}
        #count the number of frequency of each element
        for num in nums:
            if num in freq:
                freq[num] +=1

            else:
                freq[num] =1
        #find the maximum frequency
        max_freq = max(freq.values())
        #add frequencies of element having maximum frequency
        ans =0
        for count in freq.values():
            if count == max_freq:
                ans += count
        return ans
        