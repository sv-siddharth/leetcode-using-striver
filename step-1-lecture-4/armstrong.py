def is_armstrong_number(num):

  k = len(str(num))

  sum = 0

  temp = num

  while temp > 0:
    digit = temp % 10
    sum += digit ** k # sum = sum + (digit ** k)
    temp //= 10 


# Test the function
number = int(input("Enter a number: "))
if is_armstrong_number(number):
  print(number, "is an Armstrong number")
else:
  print(number, "is not an Armstrong number")