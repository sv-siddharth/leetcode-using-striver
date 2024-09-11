# https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

class Solution:
    def sumOfSeries(self, n: int) -> int:
        # Using the formula for the sum of cubes of the first n natural numbers
        sum_of_n = n * (n + 1) // 2
        return sum_of_n * sum_of_n