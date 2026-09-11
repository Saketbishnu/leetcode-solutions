class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        #recursive case
        return self.fib(n-1) + self.fib(n-2)


        