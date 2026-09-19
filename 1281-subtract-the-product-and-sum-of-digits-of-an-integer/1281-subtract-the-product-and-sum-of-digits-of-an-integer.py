class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        result =[]
        sum =0
        product =1

        while n > 0:
            digit = n % 10
            sum += digit
            product *= digit
            n =n //10
        result = product - sum
        return result
