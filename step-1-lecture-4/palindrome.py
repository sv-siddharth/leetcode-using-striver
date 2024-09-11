class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x
    
# code to find LCM of two numbers in python
# Path: step-1-lecture-4/lcm.py
# code: 
# def lcm(a,b):
#    if a>b:
#       greater = a
#   else:
#      greater = b
#  while True:
#    if greater%a == 0 and greater%b == 0:
#      lcm = greater
#     break    