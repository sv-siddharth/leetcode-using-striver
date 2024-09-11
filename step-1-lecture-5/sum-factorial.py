# https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/

def factorial(num):
    if(num<=0):
        return 1
    return num*factorial(num-1)
class Solution:
    def factorialNumbers(self, n):
        #code here 
        result=[]
        for i in range(1,n+1):
            ans=factorial(i)
            if(ans>n):
                break
            result.append(ans)
        return result