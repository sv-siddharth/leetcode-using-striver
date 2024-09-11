def sumOfDivisors(n):
    # Function to calculate the sum of all divisors of n
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

def sumOfSumOfDivisors(n):
    # Function to calculate the sum of sumOfDivisors(i) for all i from 1 to n
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += sumOfDivisors(i)
    return total_sum

# Example usage
n = 5
print(sumOfSumOfDivisors(n))  # Output: 21